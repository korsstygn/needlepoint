import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import jinja2
from base64 import b64encode
from io import BytesIO
import matplotlib.pyplot as plt
from collections import Counter

# Read the dataset from CSV
df = pd.read_csv('NewsDB-Python/datasets/dataset.csv')

# Initialize removed keywords list
removed_keywords = []

# Interactive keyword exclusion process
top_5_keywords = []
while True:
    # Display top 5 keywords and their frequencies
    if not top_5_keywords:
        # If the list is empty, initialize it with the top 5 keywords from the original dataset
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts().head(5)
        top_5_keywords = keyword_counts.index.tolist()
    else:
        # Recalculate top 5 keywords based on the original dataset (excluding discarded ones)
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts()
        top_5_keywords = [keyword for keyword, count in keyword_counts.items() if keyword not in removed_keywords][:5]
    
    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, keyword in enumerate(top_5_keywords):
        print(f"{idx + 1}. {keyword}")
    
    # Ask user if they want to remove any keyword(s)
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    
    # Parse the user input and remove specified keywords
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        removed_keywords.extend([top_5_keywords[i] for i in to_remove])
        top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")
    
    # Recalculate top 5 keywords based on the original dataset (excluding discarded ones)
    keyword_counts = all_keywords.value_counts()
    top_5_keywords = [keyword for keyword, count in keyword_counts.items() if keyword not in removed_keywords][:5]

# Task 2: Articles matching the top 5 keywords after removal
keywords_set = set(top_5_keywords)  # Use the remaining keywords
articles_top_keywords = df[df['Keywords'].apply(lambda x: any(keyword in x for keyword in keywords_set))]
print("Number of articles matching top 5 keywords:", len(articles_top_keywords))
print(articles_top_keywords.columns)

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

# Create and save word cloud image to SVG file
wordcloud = WordCloud(width=1200, height=960).generate(descriptions_top_keywords)
# Convert word cloud image to SVG
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
svg_image = BytesIO()
plt.savefig(svg_image, format='svg')
encoded_svg = b64encode(svg_image.getvalue()).decode()
wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>"
with open("NewsDB-Python/reports/Descriptions_word_cloud.html", "w") as f:
    f.write(wordcloud_svg)
print("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.html")

# Output keyword analysis report in Markdown format
report_md = f"# Keyword Analysis Report\n\n## Top 5 Keywords\n"
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
report_md += f"  - <a href='NewsDB-Python/reports/Descriptions_word_cloud.html'>**Wordcloud**</a>"
with open("NewsDB-Python/reports/keyword_analysis_report.md", "w") as f:
    f.write(report_md)
print("Markdown report saved to NewsDB-Python/reports/keyword_analysis_report.md")

# Output keyword analysis report in HTML format
if not articles_top_keywords.empty:
    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("NewsDB-Python/reports/report_template.html")
    output = template.render(keywords=top_5_keywords, articles=articles_top_keywords, author_articles=author_articles, wordcloud_svg=wordcloud_svg)
    with open("NewsDB-Python/reports/report.html", "w") as f:
        f.write(output)
    print("HTML report saved to NewsDB-Python/reports/report.html")
else:
    print("No articles found.")

