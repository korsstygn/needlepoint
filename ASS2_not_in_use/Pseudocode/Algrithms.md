# Algorithmic pseudocode versions:

1. Start
2. Read the dataset from CSV into a data structure, say DataFrame `df`.
3. Initialize an empty list to store removed keywords, let's call it `removed_keywords`.
4. Declare an empty list for top 5 keywords, let’s call this as `top_5_keywords`.
5. Start a while loop which will run until 'done' is inputted by the user.
6. If `top_5_keywords` is empty, calculate the frequency of all the keywords in `df['Keywords']` and add the top 5 into this list.
7. Display current Top Keywords and their Frequencies to the User for removal.
8. Take input from user about which keyword they want to remove.
9. If 'done' is entered by user, break the loop, else continue with the keywords selected by the user.
10. Remove the chosen keywords from `top_5_keywords` and add them into `removed_keywords`.
11. After removing necessary keywords, calculate articles matching remaining top 5 keywords after removal into a DataFrame `articles_top_keywords`.
12. Identify authors discussing these top 5 keywords by iterating through the rows of `df` and storing relevant information in a list `author_articles`.
13. Generate word cloud based on descriptions of all articles matching the remaining top 5 keywords using WordCloud library, store it into `wordcloud_svg`.
14. Write down keyword analysis report in Markdown format where Keywords, Articles and Authors are displayed along with the word cloud svg image.
15. If there is at least one article in `articles_top_keywords`, write an HTML report displaying keywords, articles matching them after removal, authors discussing top 5 keywords and the word-cloud based on descriptions of all these articles.
16. Else display a message "No articles found matching the top 5 keywords".
17. End

- - -

1. Import necessary libraries (Pandas, Matplotlib, WordCloud, etc.).
2. Load data from a CSV file into a DataFrame.
3. Initialize an empty list to store removed keywords.
4. Define an empty list for top 5 keywords.
5. Enter a loop to interactively remove keywords:
   - Display the top 5 keywords and their frequencies.
   - Prompt user for input to remove a keyword or finish the process.
   - If 'done' is entered, break the loop.
   - Otherwise, convert input to indices and add them to removed keywords list.
6. Filter articles based on the remaining top 5 keywords.
7. Identify authors discussing these top keywords and store their details in a list.
8. Generate a word cloud based on the descriptions of these articles.
9. Save the word cloud as an SVG and encode it in base64 for embedding in HTML.
10. Output a Markdown report with the top 5 keywords, articles matching these keywords, and authors discussing them.
11. Output an HTML report with similar information, including the word cloud embedded in the page.

- - -

BEGIN
  DECLARE df AS DATAFRAME BY READING 'NewsDB-Python/datasets/dataset.csv'
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
