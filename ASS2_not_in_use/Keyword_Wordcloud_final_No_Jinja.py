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
    # Display top 5 keywords and their frequencies
    if not top_5_keywords:
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts().head(5)
        top_5_keywords = keyword_counts.index.tolist()
    else:
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
articles_top_keywords = df[df['Keywords'].apply(lambda x: any(keyword in x for keyword in keywords_set))]
print("Number of articles matching top 5 keywords:", len(articles_top_keywords))


# Task 3: Identify authors discussing the top 5 keywords after removal
author_articles = []
for index, row in df.iterrows():
    for keyword in top_5_keywords:
        if str(keyword) in row['Keywords']:  # Check if keyword is in the list of top 5 keywords
            author_articles.append({
                'Keyword': keyword,
                'Author': row['Author'],
                'Title': row['Title'],
                'URL': row['Permalink'],
                'Description': row['Description'][:250]
            })
# Remove duplicates by converting to set and back to list
author_articles = [dict(t) for t in {tuple(d.items()) for d in author_articles}]

# Task 4: Word cloud based on descriptions of articles matching the remaining top 5 keywords
descriptions_top_keywords = ' '.join(articles_top_keywords['Description'].dropna())
wordcloud = WordCloud(width=1200, height=960).generate(descriptions_top_keywords)
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
svg_image = BytesIO()
plt.savefig(svg_image, format='svg')
encoded_svg = base64.b64encode(svg_image.getvalue()).decode()
wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>"
with open("NewsDB-Python/reports/Descriptions_word_cloud.html", "w") as f:
    f.write(wordcloud_svg)
print("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.html")

# Output keyword analysis report in Markdown format
report_md = f"# Keyword Analysis Report\n## Top 5 Keywords\n"
for keyword in top_5_keywords:  # Output the remaining keywords
    report_md += f"- **{keyword}**\n"
report_md += "\n## Articles Matching Top Keywords\n"
for index, row in articles_top_keywords.iterrows():
    report_md += f"- **Title**: {row['Title']}\n"
    report_md += f"  - **Author**: {row['Author']}\n"
    report_md += f"  - **Description**: {row['Description'][:250]}\n\n"
report_md += "\n## Authors Discussing Top Keywords\n"
for article in author_articles:
    report_md += f"- **Keyword**: {article['Keyword']}\n"
    report_md += f"  - **Author**: {article['Author']}\n"
    report_md += f"  - **Title**: <a href='{article['URL']}'>{article['Title']}</a>\n"
    report_md += f"  - **Description**: {article['Description']}\n\n"
report_md += "![image](NewsDB-Python/reports/Descriptions_word_cloud.svg)"
with open("NewsDB-Python/reports/keyword_analysis_report.md", "w") as f:
    f.write(report_md)
print("Markdown report saved to NewsDB-Python/reports/keyword_analysis_report.md")

# Output keyword analysis report in HTML format
if not articles_top_keywords.empty:
    html_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <link href="style_article.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,700;1,800&display=swap"
        rel="stylesheet">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keyword Analysis Report</title>
</head>
<body>
<h1 >Keyword Analysis Report</h1>
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
<h2>Task 4: Word-cloud based on descriptions of all articles</h2>

<div>{wordcloud_svg}</div>
</body>
</html>"""
    keywords = "\n".join(f'<p>{keyword}</strong></p>' for keyword in top_5_keywords)
    articles = "\n".join(f'<tr><td>{row["Title"]}</td><td>{row["Author"]}</td><td>{row["Description"][:250]}</td></tr>' for index, row in articles_top_keywords.iterrows())
    author_articles = "\n".join(f'<li>\n<strong>Keyword:</strong> {article["Keyword"]}<br>\n<strong>Author:</strong> {article["Author"]}<br>\n<strong>Title:</strong > <a href="{article["URL"]}">{article["Title"]}</a><br>\n<strong>Description:</strong > {article["Description"]}<br><br><br></li>' for article in author_articles)
    output = html_template.format(keywords=keywords, articles=articles, wordcloud_svg=wordcloud_svg, author_articles=author_articles)
    with open('NewsDB-Python/reports/report.html', 'w') as f:
        f.write(output)
    print("HTML report saved to NewsDB-Python/reports/report.html")
else:
    print("No articles found matching the top 5 keywords.")
