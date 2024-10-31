// Import required libraries
const fs = require('fs');
const csv = require('csv-parser');

// Define a function to parse CSV file and extract keywords
function parseKeywords(file) {
  return new Promise((resolve, reject) => {
    const keywordList = [];
    let counter = {};

    fs.createReadStream(file)
      .pipe(csv())
      .on('data', (row) => {
        const keywords = row.Keywords.split(';');
        keywords.forEach((keyword) => {
          if (!counter[keyword]) {
            counter[keyword] = 1;
          } else {
            counter[keyword]++;
          }
          keywordList.push(keyword);
        });
      })
      .on('end', () => {
        const tenMostCommon = Object.keys(counter).sort((a, b) => counter[b] - counter[a]).slice(0, 10);
        resolve({ keywords: keywordList, tenMostCommon, counter });
      })
      .on('error', (err) => reject(err));
  });
}

// Define a function to extract top 5 keywords from the most common ones
function getTopFive(keywords, tenMostCommon) {
  return tenMostCommon.slice(0, 5);
}

// Define a function to extract articles with top 5 keywords
function getArticlesWithTopKeywords(df, fiveMostCommon) {
  const articles = df.filter((article) => article.Keywords.includes(fiveMostCommon.join(',')));
  return articles.map((article) => ({ ...article, Description: article.Description.substring(0, 250) }));
}

// Define a function to extract top 10 authors and their keyword frequencies
function getTopTenAuthors(authors, tenMostCommon) {
  const authorCounter = {};
  authors.forEach((author) => {
    if (!authorCounter[author.Author]) {
      authorCounter[author.Author] = {};
    }
    tenMostCommon.forEach((keyword) => {
      if (author.Keywords.includes(keyword)) {
        if (!authorCounter[author.Author][keyword]) {
          authorCounter[author.Author][keyword] = 1;
        } else {
          authorCounter[author.Author][keyword]++;
        }
      }
    });
  });

  const topTenAuthors = Object.keys(authorCounter).sort((a, b) => Object.values(authorCounter[b]).reduce((sum, value) => sum + value, 0) - Object.values(authorCounter[a]).reduce((sum, value) => sum + value, 0)).slice(0, 10);
  return topTenAuthors.map((author) => ({ author, keywords: authorCounter[author] }));
}

// Define a function to write HTML content
function writeHtmlContent(df, tenMostCommon, fiveMostCommon, articlesWithTopKeywords, topTenAuthors) {
  const html = `
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>NewsDB</title>
        <link rel="stylesheet" href="styles.css">
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet">
      </head>
      <body>
        <h1>Top 10 Keywords and Frequency:</h1>
        <p>Research Questions: ${df[0].Research} Dataset Questions: ${df[0].Dataset}</p>
        <table>
          <tr>
            <th>Keyword</th>
            <th>Frequency</th>
          </tr>
          ${tenMostCommon.map((keyword, index) => `
            <tr>
              <td>${keyword}</td>
              <td>${counter[keyword]}</td>
            </tr>
          `).join('')}
        </table>

        <h1>Articles with Top 5 Keywords:</h1>
        <table>
          ${articlesWithTopKeywords.map((article) => `
            <tr>
              <td><a href="${article.Url}">${article.Title}</a></td>
              <td>${article.Description}</td>
            </tr>
          `).join('')}
        </table>

        <h1>Top 10 Authors and Their Keyword Frequency:</h1>
        ${topTenAuthors.map((author, index) => `
          <p><strong>${author.author}</strong>: ${Object.values(author.keywords).reduce((sum, value) => sum + value, 0)}</p>
          ${Object.keys(author.keywords).map((keyword, key) => `
            <p>${keyword}: ${author.keywords[key]}</p>
          `).join('')}
        `).join('')}
      </body>
    </html>
  `;
  return html;
}

// Read the CSV file and parse it
parseKeywords('NewsDB-Python/datatsets/dataset.csv')
  .then(({ keywords, tenMostCommon, counter }) => {
    const fiveMostCommon = getTopFive(keywords, tenMostCommon);
    const df = fs.readFileSync('NewsDB-Python/datatsets/dataset.csv', 'utf8').split('\n');
    const articlesWithTopKeywords = getArticlesWithTopKeywords(df.map((row) => JSON.parse(row)), fiveMostCommon);
    const authors = df.filter((article) => article.Keywords.includes(fiveMostCommon.join(',')));
    const topTenAuthors = getTopTenAuthors(authors, tenMostCommon);

    // Write the HTML content
    const html = writeHtmlContent(df, tenMostCommon, fiveMostCommon, articlesWithTopKeywords, topTenAuthors);
    fs.writeFileSync('index.html', html);
  })
  .catch((err) => console.error(err));