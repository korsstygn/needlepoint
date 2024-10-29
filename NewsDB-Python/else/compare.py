import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import jinja2
from base64 import b64encode
from io import BytesIO
import matplotlib.pyplot as plt
from collections import Counter

# Read the dataset from CSV
df = pd.read_csv('NewsDB-Python/datasets/dataset.csv')

# Task 1: Identify the top 5 keywords by frequency
keywords = df['Keywords'].str.split(';').explode().str.strip()
keyword_counts = Counter(keywords)
top_5_keywords = keyword_counts.most_common(5)
print("Top 5 keywords:", top_5_keywords)

# Interactive keyword exclusion process
while True:
    # Display top 5 keywords and their frequencies
    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, (keyword, freq) in enumerate(top_5_keywords):
        print(f"{idx + 1}. {keyword}: {freq}")
    
    # Ask user if they want to remove any keyword(s)
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    
    # Parse the user input and remove specified keywords
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        top_5_keywords = [keyword for i, keyword in enumerate(top_5_keywords) if i not in to_remove]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")

# Task 2: Articles matching the top 5 keywords
keywords_set = set([keyword for keyword, freq in top_5_keywords])
articles_top_keywords = df[df['Keywords'].apply(lambda x: any(keyword in x for keyword in keywords_set))]

# Task 3: Identify authors discussing the top 5 keywords and list their articles
author_articles = []
for index, row in df.iterrows():
    for keyword in top_5_keywords:
        if str(keyword[0]) in row['Keywords']:
            author_articles.append({
                'Keyword': keyword[0],
                'Author': row['Author'],
                'Title': row['Title'],
                'URL': row['Permalink'],
                'Description': row['Description'][:250]
            })
# Remove duplicates by converting to set and back to list
author_articles = [dict(t) for t in {tuple(d.items()) for d in author_articles}]

# Task 4: Word cloud based on descriptions of articles matching the top 5 keywords or all articles
all_descriptions = ' '.join(df['Description'].dropna())
top_keywords_only = ' '.join([keyword for keyword, freq in top_5_keywords])
all_descriptions_top = all_descriptions + ' ' + top_keywords_only

# Create and save word cloud image to SVG file
wordcloud = WordCloud(width=1200, height=960).generate(all_descriptions_top)
# Convert word cloud image to SVG
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
svg_image = BytesIO()
plt.savefig(svg_image, format='svg')
encoded_svg = b64encode(svg_image.getvalue()).decode()
wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>"
with open("NewsDB-Python/reports/Descriptions_word_cloud.svg", "w") as f:
    f.write(wordcloud_svg)
print("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.svg")

# Output keyword analysis report in Markdown format
report_md = f"# Keyword Analysis Report\n\n## Top 5 Keywords\n"
for keyword, freq in top_5_keywords:
    report_md += f"- **{keyword}**: {freq}\n"
report_md += "\n## Articles Matching Top Keywords\n"
for index, row in articles_top_keywords.iterrows():
    report_md += f"- **Title**: {row['Title']}\n"
    report_md += f"  - **Author**: {row['Author']}\n"
    report_md += f"  - **Description**: {row['Description'][:250]}\n\n"
report_md += "\n## Authors Discussing Top Keywords\n"
for article in author_articles:
    report_md += f"- **Keyword**: {article['Keyword']}\n"
    report_md += f"  - **Author**: {article['Author']}\n"
    report_md += f"  - **Title**: {article['Title']}\n"
    report_md += f"  - **URL**: <a href='{article['URL']}'>{article['URL']}</a>\n"
    report_md += f"  - **Description**: {article['Description']}\n\n"
with open("NewsDB-Python/reports/keyword_analysis_report.md", "w") as f:
    f.write(report_md)
print("Markdown report saved to NewsDB-Python/reports/keyword_analysis_report.md")

# Output keyword analysis report in HTML format
template_loader = jinja2.FileSystemLoader(searchpath=".")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("NewsDB-Python/reports/report_template.html")
output = template.render(keywords=top_5_keywords, articles=articles_top_keywords, author_articles=author_articles)
with open("NewsDB-Python/reports/report.html", "w") as f:
    f.write(output)
print("HTML report saved to NewsDB-Python/reports/report.html")
