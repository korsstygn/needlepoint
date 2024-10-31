import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from markdown import markdown
from jinja2 import Template

# Load the dataset
articles = pd.read_csv("NewsDB-Python/datasets/news_articles.csv")

# Extract top keywords and authors
top_keywords = articles.groupby(["Keyword"])["Description"].count().sort_values(ascending=False).head(5)
author_articles = articles.groupby(["Author", "Keyword"])["Title"].count().reset_index()

# Generate word cloud for top keywords
wordcloud = WordCloud(width=800, height=400, stopwords=STOPWORDS).generate_from_frequencies(top_keywords.to_dict())
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Display the top keywords and authors
print("Top Keywords:")
print(top_keywords)
print("\nTop Authors:")
print(author_articles["Author"].value_counts().head(5))

# Filter articles that match top keywords
articles_top_keywords = articles[articles["Keyword"].isin(top_keywords.index)]

# Generate Markdown report for articles matching top keywords
md_output = f"## Task 2: Articles Matching Top Keywords\n\n"
for index, row in articles_top_keywords.iterrows():
    md_output += f"- **Title**: <a href='{row['URL']}'>{row['Title']}</a>\n"
    md_output += f"  - **Author**: {row['Author']}\n"
    md_output += f"  - **Description**: {row['Description'][:250]}\n\n"

# Generate Markdown report for authors discussing top keywords
md_author_keywords = f"## Task 3: Authors Discussing Top Keywords\n\n"
for index, row in author_articles.iterrows():
    md_author_keywords += f"- **Author**: {row['Author']}\n"
    md_author_keywords += f"- **Keyword**: {row['Keyword']}\n"
    md_author_keywords += f"- **Title**: <a href='{articles[articles['Author'] == row['Author']].loc[0]['URL']}'>{articles[articles['Author'] == row['Author']].loc[0]['Title']}</a>\n"
    md_author_keywords += f"- **Description**: {articles[articles['Author'] == row['Author']].loc[0]['Description'][:250]}\n\n"

# Save Markdown reports to files
with open("NewsDB-Python/reports/keyword_analysis_report.md", "w") as f:
    f.write(md_output)
with open("NewsDB-Python/reports/authors_discussing_keywords_report.md", "w") as f:
    f.write(md_author_keywords)

# Generate HTML report using Jinja2 templating engine
html_template = """
<!DOCTYPE html>
<html>
<head>
  <title>NewsDB-Python Report</title>
</head>
<body>
  <h1>Top Keywords and Authors</h1>
  <p>Top keywords:</p>
  <ul>
    {% for keyword in top_keywords %}
      <li>{{ keyword }}</li>
    {% endfor %}
  </ul>
  <p>Top authors:</p>
  <ul>
    {% for author in author_articles["Author"].value_counts().head(5) %}
      <li>{{ author }} ({{ articles[articles['Author'] == author]['Keyword'].unique().shape[0] }})</li>
    {% endfor %}
  </ul>
  <h1>Articles Matching Top Keywords</h1>
  <p>Here are the articles that match the top keywords:</p>
  <ol>
    {% for index, row in articles_top_keywords.iterrows() %}
      <li><a href="{{ row['URL'] }}">{{ row['Title'] }}</a></li>
    {% endfor %}
  </ol>
  <h1>Authors Discussing Top Keywords</h1>
  <p>Here are the authors who have written articles that match the top keywords:</p>
  <ol>
    {% for index, row in author_articles.iterrows() %}
      <li><a href="{{ articles[articles['Author'] == row['Author']].loc[0]['URL'] }}">{{ row['Author'] }}</a></li>
    {% endfor %}
  </ol>
</body>
</html>
"""

jinja_template = Template(html_template)
html_output = jinja_template.render(top_keywords=top_keywords, author_articles=author_articles)

# Save HTML report to file
with open("NewsDB-Python/reports/newsdb_python_report.html", "w") as f:
    f.write(html_output)