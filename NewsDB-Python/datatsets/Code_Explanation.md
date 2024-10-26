# The code step-by-step

```Python
import pandas as pd  # Importing the Pandas library for data manipulation and analysis
from collections import Counter  # Importing Counter from the collections module to count frequencies of elements
from operator import itemgetter  # Importing itemgetter for easier access of list items in a specific position

# read csv file into dataframe
df = pd.read_csv('NewsDB-Python/datatsets/dataset.csv')  # Reading the CSV file into a DataFrame, replace 'filepath' with your actual CSV filename
```

- **Explanation**: We use `pd.read_csv` to load the CSV file into a DataFrame, which is a 2D tabular data structure with labeled axes (rows and columns).

```Python
# TASK 1: Which 10 keywords occur most frequently in the dataset?
keywords = df['Keywords'].str.split(';')  # Splitting the 'Keywords' column by semicolon to handle multiple keywords per entry
keyword_list = [item for sublist in keywords for item in sublist]  # Flattening the list of lists into a single list
counter = Counter(keyword_list)  # Counting the frequency of each keyword using Counter from collections
ten_most_common = counter.most_common(10)  # Getting the 10 most common keywords
```

- **Explanation**: We use `str.split(';')` to split the keywords stored as a single string into individual words (keywords) based on the semicolon delimiter. The list of lists is then flattened into a single list using a list comprehension.
- **Explanation**: We use `Counter` from the `collections` module to count how many times each keyword appears in the dataset.
- **Explanation**: `most_common(10)` returns a list of the 10 most common elements and their counts from the `Counter` object.

```Python
# TASK 2: Which articles match the five most frequently occurring keywords?
five_most_common = [item[0] for item in ten_most_common[:5]]  # Extracting the top 5 common keywords
articles_with_top_keywords = df.loc[df['Keywords'].str.contains('|'.join(five_most_common)), ['Keywords', 'Title', 'Author', 'Description']]  # Filtering the DataFrame to include articles with any of the top 5 keywords
# limit description length to 250 characters
articles_with_top_keywords['Description'] = articles_with_top_keywords['Description'].str[:250]
```

- **Explanation**: We extract the top 5 common keywords by slicing `ten_most_common` and using list comprehension to create a list of these keywords.
- **Explanation**: We use `str.contains('|'.join(five_most_common))` to filter the DataFrame where the 'Keywords' column contains any of the top 5 keywords.
- **Explanation**: We limit the description length to 250 characters for better display in HTML.

```Python
# TASK 3: Which authors discuss the ten most common keywords? How many are there and what are their names?
authors = df.loc[df['Keywords'].str.contains('|'.join(keyword for keyword, freq in ten_most_common)), 'Author']  # Filtering to include authors with any of the top 10 keywords
author_counter = Counter(authors)  # Counting frequencies of authors using Counter from collections
top_ten_authors = author_counter.most_common(10)  # Getting the top 10 authors using these keywords
```

- **Explanation**: We filter the DataFrame to include only those rows where the 'Keywords' contain any of the top 10 keywords.
- **Explanation**: We count the frequency of each author using `Counter`.
- **Explanation**: `most_common(10)` returns the top 10 authors using these keywords.

```Python
# output results to HTML file
with open('index.html', 'w') as f:  # Opening a file named index.html to write HTML content
    f.write('<!DOCTYPE html><html lang="sv"><head><title>Dataset analysis</title>'
            '<link href="css/style_article.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,700;1,800&display=swap" rel="stylesheet"></head>')
    f.write('<body><h1>Top 10 keywords and their frequency</h1><p><strong>Research question:</strong> What five issues is the academic literature selected for our dataset most critical of when it comes to Google?<br><strong>Dataset question:</strong> Which 5 keywords occur most frequently in the dataset?</p>')
    f.write(pd.DataFrame(ten_most_common, columns=['Keyword', 'Frequency']).to_html(index=False))  # Writing the top 10 keywords to HTML file
    f.write('<h1>Articles that contain the top 5 keywords</h1><p><strong>Research question:</strong>How much and what has been published in the academic literature selected for our dataset about these top issues of concern?<br><strong>Dataset question:</strong> Which articles match the five most frequently occurring keywords? <em>List the number of articles and their individual titles</em></p>')
    f.write(articles_with_top_keywords.to_html(index=False))  # Writing articles with top 5 keywords to HTML file
    f.write('<h1>Top 10 authors and their keyword frequency</h1><p><strong>Research question:</strong>How many authors in our dataset are most interested in or write about these top issues of concern? List the the top ten keywords and the authors, as well as the titles and permalinks<br><strong>Dataset question:</strong> Which authors discuss the ten most common keywords? How many are there and what are their names? List the the top ten keywords and the authors, as well as the titles and permalinks as in the example above.<em>List the number of articles and their individual titles</em></p>')
    f.write('<h1>Top keywords per author</h1><p><strong>Research question:</strong> Which keywords does each of top 10 authors use frequently?<br /><em>List the number of times the authors use these keywords and their individual titles</em></p>')
    for i, (author, frequency) in enumerate(top_ten_authors):  # Looping through top 10 authors
        author_keywords = df.loc[df['Author'] == author, 'Keywords'].str.split(';')  # Getting the keywords for each author
        author_keyword_list = [item for sublist in author_keywords for item in sublist]  # Flattening the list of lists
        counter = Counter(author_keyword_list)  # Counting frequencies of keywords for each author
        top_five_author_keywords = counter.most_common(5)  # Getting the five most common keywords by this author
        f.write('<strong>' + 'Author '+ str(i+1) + ': ' + '</strong>' + author + pd.DataFrame(top_five_author_keywords, columns=['Keyword', 'Frequency']).to_html(index=False))  # Writing top 5 authors' keywords to HTML file
```

- **Explanation**: We open an HTML file named `index.html` for writing and start constructing the HTML content using Python's string manipulation capabilities within the file.
- **Explanation**: We use `pd.DataFrame` to convert lists into a table format and write it directly to the HTML file using `to_html`.
- **Explanation**: We loop through each of the top 10 authors, extract their keywords, count their frequencies, and write them to the HTML file.

## Pseudocode

1. Load a CSV file into a DataFrame.
2. Split the 'Keywords' column by semicolon to get individual keywords.
3. Count the frequency of each keyword using a Counter.
4. Determine the 10 most common keywords and store them for reference.
5. Filter articles containing any of the top 5 most common keywords, and shorten descriptions to 250 characters.
6. List all authors who discuss the top 10 most common keywords and count their usage frequency.
7. Identify the top 10 authors by keyword usage and prepare a report to be saved as an HTML file.
8. Write the following in the HTML file:
   - Introduction with research and dataset questions.
   - Table of top 10 keywords and frequencies.
   - List of articles with the top 5 most frequent keywords.
   - Details about the top 10 authors, including their keyword usage frequency and associated articles.

```Algorithmic Pseudocode
1. Import necessary libraries:
   a. import pandas as pd
   b. from collections import Counter
   c. from operator import itemgetter
   
2. Read the CSV file into a DataFrame:
   df = pd.read_csv('NewsDB-Python/datatsets/dataset.csv')
   
3. TASK 1: Extract and count the most frequent keywords in the dataset:
   a. Split the 'Keywords' column by semicolon to get individual keywords for each entry:
      keywords = df['Keywords'].str.split(';')
   
   b. Flatten the list of lists into a single list:
      keyword_list = [item for sublist in keywords for item in sublist]
   
   c. Count the frequency of each keyword:
      counter = Counter(keyword_list)
   
   d. Get the 10 most common keywords:
      ten_most_common = counter.most_common(10)
   
4. TASK 2: Filter articles that match the top 5 most frequent keywords:
   a. Extract the top 5 common keywords from ten_most_common:
      five_most_common = [item[0] for item in ten_most_common[:5]]
   
   b. Filter the DataFrame to include only articles with any of the top 5 keywords:
      articles_with_top_keywords = df.loc[df['Keywords'].str.contains('|'.join(five_most_common)), ['Keywords', 'Title', 'Author', 'Description']]
   
   c. Limit the description length to 250 characters:
      articles_with_top_keywords['Description'] = articles_with_top_keywords['Description'].str[:250]
   
5. TASK 3: Identify authors discussing the top 10 most common keywords and count their frequency:
   a. Filter the DataFrame to include authors with any of the top 10 keywords:
      authors = df.loc[df['Keywords'].str.contains('|'.join(keyword for keyword, freq in ten_most_common)), 'Author']
   
   b. Count the frequency of each author:
      author_counter = Counter(authors)
   
   c. Get the top 10 authors using these keywords:
      top_ten_authors = author_counter.most_common(10)
   
6. Output the results to an HTML file:
   a. Open an HTML file named index.html for writing:
      with open('index.html', 'w') as f:
   
   b. Construct the HTML content and write it to the file:
      f.write('<!DOCTYPE html><html lang="sv"><head>...')  # (HTML boilerplate)
      f.write('<h1>Top 10 keywords and their frequency</h1>...')
      f.write(pd.DataFrame(ten_most_common, columns=['Keyword', 'Frequency']).to_html(index=False))
      f.write('<h1>Articles that contain the top 5 keywords</h1>...')
      f.write(articles_with_top_keywords.to_html(index=False))
      f.write('<h1>Top 10 authors and their keyword frequency</h1>...')
      for i, (author, frequency) in enumerate(top_ten_authors):
         author_keywords = df.loc[df['Author'] == author, 'Keywords'].str.split(';')
         author_keyword_list = [item for sublist in author_keywords for item in sublist]
         counter = Counter(author_keyword_list)
         top_five_author_keywords = counter.most_common(5)
         f.write('<strong>' + 'Author '+ str(i+1) + ': ' + '</strong>' + author + pd.DataFrame(top_five_author_keywords, columns=['Keyword', 'Frequency']).to_html(index=False))
```

```Algorithmic Pseudocode
BEGIN
   DECLARE df AS DATAFRAME BY READING 'NewsDB-Python/datatsets/dataset.csv'
   DECLARE keywords AS LIST OF STRINGS BY SPLITTING 'Keywords' COLUMN BY ';'
   DECLARE keyword_list AS LIST OF STRINGS BY FLATTENING keywords
   DECLARE counter AS COUNTER FOR keyword_list
   SET ten_most_common TO counter.MOST_COMMON(10)

   DECLARE five_most_common AS LIST OF STRINGS BY EXTRACTING KEYWORDS FROM ten_most_common[0:5]
   SET articles_with_top_keywords TO df WHERE 'Keywords' CONTAINS ANY OF five_most_common
   SET articles_with_top_keywords['Description'] TO FIRST 250 CHARACTERS OF articles_with_top_keywords['Description']

   DECLARE authors AS LIST OF STRINGS BY FILTERING df WHERE 'Keywords' CONTAINS ANY OF keywords IN ten_most_common
   SET author_counter AS COUNTER FOR authors
   SET top_ten_authors TO author_counter.MOST_COMMON(10)

   OPEN FILE 'index.html' FOR WRITING
   WRITE HTML CONTENT INCLUDING:
      - HEAD WITH TITLE, STYLESHEETS, AND FONTS
      - BODY CONTAINING:
         - H1 FOR TOP 10 KEYWORDS AND FREQUENCY
         - P WITH RESEARCH AND DATASET QUESTIONS
         - TABLE OF ten_most_common
         - H1 FOR ARTICLES WITH TOP 5 KEYWORDS
         - TABLE OF articles_with_top_keywords
         - H1 FOR TOP 10 AUTHORS AND THEIR KEYWORD FREQUENCY
         - LOOP THROUGH top_ten_authors TO:
            - LIST THEIR ASSOCIATED KEYWORDS AND FREQUENCIES
            - WRITE ARTICLES FOR EACH AUTHOR AS NECESSARY
   CLOSE FILE
END
```
