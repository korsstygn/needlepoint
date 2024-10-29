import pandas as pd
from collections import Counter

# read csv file into dataframe
df = pd.read_csv('NewsDB-Python/datatsets/dataset.csv')  # replace 'filepath' with your actual CSV filename 

# TASK 1: Which 10 keywords occur most frequently in the dataset?
keywords = df['Keywords'].str.split(';') # splitting by semicolon as we assume that is the splitter for multiple entries
keyword_list = [item for sublist in keywords for item in sublist]  # flattening list of lists into a single list 
counter = Counter(keyword_list)  # counting frequencies using collection's counter
ten_most_common = counter.most_common(10) # getting the ten most common

# TASK 2: Which articles match the five most frequently occurring keywords?
five_most_common = [item[0] for item in ten_most_common[:5]]  # getting the top 5 common keywords only
# repeat five_most_common until it is the same size as df
articles_with_top_keywords = df.loc[df['Keywords'].str.contains('|'.join(five_most_common)), ['Title', 'Author', 'Description', 'Permalink']]
articles_with_top_keywords = articles_with_top_keywords.assign(Keywords=five_most_common)
# limit description length to 250 characters
articles_with_top_keywords['Description'] = articles_with_top_keywords['Description'].str[:250]

# TASK 3: Which authors discuss the ten most common keywords? How many are there and what are their names?
authors = df.loc[df['Keywords'].str.contains('|'.join(keyword for keyword, freq in ten_most_common)), 'Author'] # filtering dataframe to include authors with any of the ten most frequent keywords
author_counter = Counter(authors)  # counting frequencies of authors
top_ten_authors = author_counter.most_common(10) # getting top 10 authors that use these keywords

# create a dataframe for top ten authors and their frequencies, add the new 'Keywords' column to it with all 10 common keywords only
top_author_df = pd.DataFrame(top_ten_authors, columns=['Author', 'Frequency'])
top_author_df['Keywords'] = [keyword for keyword, freq in ten_most_common]  

# output results to HTML file with added CSS and HTML structure
with open('results.html', 'w') as f:
    f.write('<!DOCTYPE html><html lang="sv"><head><title>Dataset analysis</title>'
            '<link href="css/style_article.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,700;1,800&display=swap" rel="stylesheet"></head>')
    f.write('<body><h1 style="font-size: 2em; color: blue;">Top 10 keywords and their frequency</h1>')
    # write top 10 keywords to HTML file, with a custom CSS class for styling the table
    f.write(pd.DataFrame(ten_most_common, columns=['Keyword', 'Frequency']).to_html(index=False, classes='table table-striped'))  
    f.write('<h1 style="font-size: 2em; color: blue;">Articles that contain the top 5 keywords</h1>')
    # write articles with top 5 keywords to HTML file, with a custom CSS class for styling the table
    articles_with_top_keywords.to_html(index=False, classes='table table-striped', col_space=3) 
    f.write('<h1 style="font-size: 2em; color: blue;">Top 10 authors and their keyword frequency</h1>')
    # write top 10 authors to HTML file, with a custom CSS class for styling the table
    top_author_df.to_html(index=False, classes='table table-striped', col_space=3)  