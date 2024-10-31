import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from collections import Counter
import re

# Read the dataset from CSV
df = pd.read_csv('NewsDB-Python/datasets/dataset.csv')

# Initialize removed keywords list
removed_keywords = []

# Interactive keyword exclusion process
top_5_keywords = []
while True:
    # Task 1: Display top 5 keywords and their frequencies
    if not top_5_keywords:  # If the top 5 keywords are not yet populated
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts().head(5)
        top_5_keywords = keyword_counts.index.tolist()
    else:  # If we already have top 5 keywords, remove those that the user has marked for removal
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts()
        top_5_keywords = [keyword for keyword, count in keyword_counts.items() if keyword not in removed_keywords][:5]
    
    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, keyword in enumerate(top_5_keywords):
        print(f"{idx + 1}. {keyword}")
        
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        removed_keywords.extend([top_5_keywords[i] for i in to_remove])
        top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")

# Task 2: Articles matching the top 5 keywords after removal
keywords_set = set(top_5_keywords)  # Use the remaining keywords
articles_top_keywords = df[df['Keywords'].apply(lambda x: any(keyword in x for keyword in keywords_set))] # filter articles where at least one keyword is found in 'Keywords' column 
print("Number of articles matching top 5 keywords:", len(articles_top_keywords))
# Task 3: Identify authors discussing the top 5 keywords after removal
author_articles = []  # list to store relevant information from each article
for index, row in df.iterrows():  # iterate through rows of dataframe df
    for keyword in top_5_keywords: # for every keyword in top 5 remaining keywords
        if str(keyword) in row['Keywords']: # check if the keyword is present in 'Keywords' column of current row
            author_articles.append({  # if so, add relevant info to author_articles list
                'Keyword': keyword,
                'Author': row['Author'],
                'Title': row['Title'], 
                'URL': row['Permalink'],
                'Description': row['Description'] # 'Description': row['Description'][:250]  # Uncomment this line to limit description length to first 250 characters
            })
author_articles = [dict(t) for t in {tuple(d.items()) for d in author_articles}]  # Remove duplicates by converting to set and back to list

# Task 4: Word cloud based on descriptions of articles matching the remaining top 5 keywords
descriptions_top_keywords = ' '.join(articles_top_keywords['Description'].dropna()) # join all descriptions in a single string, dropping NaNs
wordcloud = WordCloud(width=1200, height=960).generate(descriptions_top_keywords)  # generate word cloud with the joined descriptions
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
svg_image = BytesIO()
plt.savefig(svg_image, format='svg') # Save word cloud as svg image
encoded_svg = base64.b64encode(svg_image.getvalue()).decode()  # Encoding the svg image to display in HTML report
wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>" 
with open("NewsDB-Python/reports/Descriptions_word_cloud.html", "w") as f: # Save image in html report
    f.write(wordcloud_svg)
print("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.html") 

# Output keyword analysis report in Markdown format
report_md = f"# Keyword Analysis Report\n## TASK 1: Display the top 5 keywords and their frequencies.\n### Which five keywords occur most frequently in the dataset?\n\n"
for keyword in top_5_keywords:  # Output the remaining keywords
    report_md += f". {keyword}\n\n"
report_md += "## TASK 2: Articles matching the top 5 keywords \n### Which articles match the five most frequently occurring keywords?\n\n"
for index, row in articles_top_keywords.iterrows():  # Output titles, authors and descriptions of relevant articles
    report_md += f"- #### Title: <a href='{row['Permalink']}'>{row['Title']}</a>\n" 
    report_md += f"**Author**: {row['Author']}\n"
    report_md += f" **|** "
    report_md += f"**Description**: {row['Description']}\n\n"
report_md += "## TASK 3: Identify authors discussing the top 5 keywords\n### Which authors discuss the top five keywords?\n\n"
for article in author_articles:  # Output relevant info from each article in author_articles list
    report_md += f"- **Keyword**: {article['Keyword']}\n"   
    report_md += f"  - **Author**: {article['Author']}\n"
    report_md += f"  - **Title**: <a href='{article['URL']}'>{article['Title']}</a>\n" 
    report_md += f"  - **Description**: {article['Description']}\n\n"   
report_md += "TASK 4: Word cloud based on descriptions of All articles\n![image](NewsDB-Python/reports/Descriptions_word_cloud.svg)\n"
with open("NewsDB-Python/reports/keyword_analysis_report.md", "w") as f:  # Save markdown report 
    f.write(report_md)
print("Markdown report saved to NewsDB-Python/reports/keyword_analysis_report.md")

# Output keyword analysis report in HTML format
html_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <link href="style_article.css" rel="stylesheet">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keyword Analysis Report</title>
</head>
<body>
<h1>Keyword Analysis Report</h1>
<h2>Task 1: Top 5 Keywords</h2>
<p>{keywords}</p>
<h2>Task 2: Articles Matching Top Keywords</h2>
<table>
  <tr>
    <th>Title</th>
    <th>Author</th>
    <th>Description</th>
  </tr>
{articles}
</table>
<h2>Task 3: Authors Discussing Top Keywords</h2>
{author_articles}
<h2>Task 4: Word cloud based on descriptions of all articles matching the keywords</h2>
<div>{wordcloud}</div>
</body>
</html>"""  # HTML template with placeholders for various parts of report
keywords = "\n".join(f'<p>{keyword}</p>' for keyword in top_5_keywords) 
articles = "\n".join(f'<tr ><td><a href="{row["Permalink"]}">{row["Title"]}</a></td><td>{row["Author"]}</td><td>{row["Description"]}</td></tr>' for index, row in articles_top_keywords.iterrows())  
author_articles = "\n".join(f'<li ><h3>Keyword: {article["Keyword"]}</h3><p>Author: {article["Author"]}</p><p>Title: <a href="{article["URL"]}">{article["Title"]}</a></p><p>Description: {article["Description"]}</p></li>' for article in author_articles)  
output = html_template.format(keywords=keywords, articles=articles, wordcloud=wordcloud_svg, author_articles=author_articles) # Format the HTML template with the actual data
with open('NewsDB-Python/reports/report.html', 'w') as f:  # Save the html report 
    f.write(output)
print("HTML report saved to NewsDB-Python/reports/report.html")   
