import pandas as pd
from collections import Counter

# read_csv(file_path):
# Reads data from a CSV file into a pandas DataFrame.

# list_keywords(df):
# Extracts keywords from the 'Keywords' column of a DataFrame, split by ';', and flattens into a single series.

# tally_keyword_frequency(keywords):
# Counts the frequency of each keyword in the series and returns the top 5 most common ones.
# count_articles(df, top_keywords):
# Counts articles that match any of the top keywords in the 'Title' column and return their titles and authors.

# list_authors(df):
# Extracts authors from the 'Author' column of a DataFrame, split by ';', and flattens into a single series.
# generate_html_output(top_keywords, articles_matching_keywords, top_authors):
# Generates an HTML report summarizing the analysis of keywords and authors.

# write_html_to_file(html, output_path):
# Writes the HTML content to an output file.

# main block:
# Reads data from a CSV file, performs analysis, generates HTML, and writes it to a file.

def read_csv(file_path):
 # Read data from a CSV file into a pandas DataFrame.
    
    return pd.read_csv(file_path)
def list_keywords(df):
# Extract keywords from the 'Keywords' column of a DataFrame, split by ';', and flatten into a single series.

    keywords = df['Keywords'].str.split(';', expand=True).stack().dropna()
    return keywords

def tally_keyword_frequency(keywords):
 # Count the frequency of each keyword in the series and return the top 5 most common ones.
    
    keyword_counts = Counter(keywords)
    most_common_keywords = keyword_counts.most_common(5)
    return most_common_keywords

def count_articles(df, top_keywords): 
    # Count articles that match any of the top keywords in the 'Title' column and return their titles and authors.
    # Use regex to find any of the top keywords in the article titles
    
    article_counts = df['Title'].str.contains('|'.join(top_keywords), na=False).sum()
    # Filter articles that match the top keywords and select their titles and authors
    articles_matching_keywords = df[df['Title'].str.contains('|'.join(top_keywords), na=False)][['Title', 'Author']]
    
    return article_counts, articles_matching_keywords

def list_authors(df):
 # Extract authors from the 'Author' column of a DataFrame, split by ';', and flatten into a single series.
    
    authors = df['Author'].str.split(';', expand=True).stack().dropna()
    author_counts = Counter(authors)
    most_common_authors = author_counts.most_common(5)
    return most_common_authors

def generate_html_output(top_keywords, articles_matching_keywords, top_authors):
    # Generate an HTML report summarizing the analysis of keywords and authors.
    html = f"""
    <html>
    <head>
        <title>Dataset analysis</title>
        <link href="css/style_article.css" rel="stylesheet">
        <link
            href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,700;1,800&display=swap"
            rel="stylesheet">
    </head>
    <body>
        <h1>Task 1: Most Frequent Keywords</h1>
        <p><strong>Research question:</strong> What five issues is the academic literature selected for our dataset most critical of when it comes to Google?<br><strong>Dataset question:</strong> Which 5 keywords occur most frequently in the dataset?</p>
        <ol>
    """
    
    # List top 5 keywords with their counts (Task 1)
    for keyword, count in top_keywords:
        html += f"            <li>{keyword} ({count})</li>\n"

    html += "        </ol>\n\n"

    html += "<h1>Task 2: Articles Matching Top Keywords</h1>"
    html += "<p><strong>Research question:</strong>How much and what has been published in the academic literature selected for our dataset about these top issues of concern?<br><strong>Dataset question:</strong> Which articles match the five most frequently occurring keywords? <em>List the number of articles and their individual titles</em></p> "
    html += f"<h3>Total articles matching top keywords: {articles_matching_keywords.shape[0]}</h3>\n"
    html += "<table border='1'>\n"
    html += "        <tr><th>Title</th><th>Author</th></tr>\n"
    # - - - - - - - - - - - - - - - - - - - - - - -  END Task 1
    # List titles and authors of articles that match the top keywords (Task 2)
    for title, author in articles_matching_keywords.values:
        html += f"        <tr><td>{title}</td><td>{author}</td></tr>\n"

    html += "    </table>\n\n"

    html += "<h1>Task 3: Authors Discussing Top Keywords</h1>"
    html += "<ul>\n"
        # - - - - - - - - - - - - - - - - - - - - - - -  END Task 2
    # List each keyword and its associated authors with their counts (Task 3)
    for keyword, _ in top_keywords:
        html += f"            <li><strong>{keyword}</strong></li>\n"
        for author, count in filter(lambda x: x[0] in articles_matching_keywords['Author'].values, top_authors):
            html += f"                <ul><li>{author} ({count})</li></ul>\n"
    html += "        </ul>\n\n"
    # - - - - - - - - - - - - - - - - - - - - - - -  END Task 3
    html += "</body></html>"
    return html #End of HTML generation

def write_html_to_file(html, output_path):
# Write the HTML content to an output file.

    with open(output_path, 'w') as file:
        file.write(html)

if __name__ == "__main__":
    input_csv = 'NewsDB-Python/datatsets/dataset.csv'
    output_html = 'output.html'

    df = read_csv(input_csv)
    keywords = list_keywords(df)
    top_keywords = tally_keyword_frequency(keywords)
    article_counts, articles_matching_keywords = count_articles(df, [kw[0] for kw in top_keywords])
    top_authors = list_authors(df)

    html_output = generate_html_output(top_keywords, articles_matching_keywords, top_authors)
    write_html_to_file(html_output, output_html)

    print(f"Results have been written to {output_html}")
