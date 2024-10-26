import pandas as pd
from collections import Counter
from operator import itemgetter

# read csv file into dataframe
df = pd.read_csv('NewsDB-Python/datatsets/dataset.csv') # replace 'filepath' with your actual CSV filename 

# TASK 1: Which 10 keywords occur most frequently in the dataset?
keywords = df['Keywords'].str.split(';') # splitting by semicolon as we assume that is the splitter for multiple entries
keyword_list = [item for sublist in keywords for item in sublist]  # flattening list of lists into a single list 
counter = Counter(keyword_list)  # counting frequencies using collection's counter
ten_most_common = counter.most_common(10) # getting the ten most common

# TASK 2: Which articles match the five most frequently occurring keywords?
five_most_common = [item[0] for item in ten_most_common[:5]]  # getting the top 5 common keywords only
articles_with_top_keywords = df.loc[df['Keywords'].str.contains('|'.join(five_most_common)), ['Keywords','Title', 'Author', 'Description']] # filtering dataframe to include articles with any of the five most frequent keywords
# limit description length to 250 characters
articles_with_top_keywords['Description'] = articles_with_top_keywords['Description'].str[:250]


# TASK 3: Which authors discuss the ten most common keywords? How many are there and what are their names?
authors = df.loc[df['Keywords'].str.contains('|'.join(keyword for keyword, freq in ten_most_common)),'Author'] # filtering dataframe to include authors with any of the ten most frequent keywords
author_counter = Counter(authors)  # counting frequencies of authors
top_ten_authors = author_counter.most_common(10) # getting top 10 authors that use these keywords

# output results to HTML file
with open('index.html', 'w') as f:
    f.write('<!DOCTYPE html><html lang="sv"><head><title>Dataset analysis</title>'
            '<link href="css/style_article.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,700;1,800&display=swap" rel="stylesheet"></head>')
    f.write('<body><h1>Top 10 keywords and their frequency</h1><p><strong>Research question:</strong> What five issues is the academic literature selected for our dataset most critical of when it comes to Google?<br><strong>Dataset question:</strong> Which 5 keywords occur most frequently in the dataset?</p>')
    f.write(pd.DataFrame(ten_most_common, columns=['Keyword', 'Frequency']).to_html(index=False))  # write top 10 keywords to HTML file
    f.write('<h1>Articles that contain the top 5 keywords</h1><p><strong>Research question:</strong>How much and what has been published in the academic literature selected for our dataset about these top issues of concern?<br><strong>Dataset question:</strong> Which articles match the five most frequently occurring keywords? <em>List the number of articles and their individual titles</em></p>')
    f.write(articles_with_top_keywords.to_html(index=False)) # write articles with top 5 keywords to HTML file
    f.write('<h1>Top 10 authors and their keyword frequency</h1><p><strong>Research question:</strong>How many authors in our dataset are most interested in or write about these top issues of concern? List the the top ten keywords and the authors, as well as the titles and permalinks<br><strong>Dataset question:</strong> Which authors discuss the ten most common keywords? How many are there and what are their names? List the the top ten keywords and the authors, as well as the titles and permalinks as in the example above.<em>List the number of articles and their individual titles</em></p>')

    f.write('<h1>Top keywords per author</h1><p><strong>Research question:</strong> Which keywords does each of top 10 authors use frequently?<br /><em>List the number of times the authors use these keywords and their individual titles</em></p>')
    for i, (author, frequency) in enumerate(top_ten_authors):
        author_keywords = df.loc[df['Author'] == author, 'Keywords'].str.split(';')
        author_keyword_list = [item for sublist in author_keywords for item in sublist]
        counter = Counter(author_keyword_list)  # counting frequencies using collection's counter
        top_five_author_keywords = counter.most_common(5) # getting the five most common by this author
        f.write('<strong>' + 'Author '+ str(i+1) + ': ' + '</strong>' + author + pd.DataFrame(top_five_author_keywords, columns=['Keyword', 'Frequency']).to_html(index=False))  # write top 5 authors' keywords to HTML file
        # f.write(pd.DataFrame(top_ten_authors, columns=['Author', 'Frequency']).to_html(index=False))  # write top 10 authors to HTML file

