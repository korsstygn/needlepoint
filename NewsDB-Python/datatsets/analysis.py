import pandas as pd
from collections import Counter

def read_csv(file_path):
    return pd.read_csv(file_path)

def list_keywords(df):
    keywords = df['Keywords'].str.split(';', expand=True).stack().dropna()
    return keywords

def tally_keyword_frequency(keywords):
    keyword_counts = Counter(keywords)
    most_common_keywords = keyword_counts.most_common(5)
    return most_common_keywords

def count_articles(df, top_keywords):
    # We don't need Permalink for Task 2. So, this function is simplified.
    article_counts = df['Title'].str.contains('|'.join(top_keywords), na=False).sum()
    articles_matching_keywords = df[df['Title'].str.contains('|'.join(top_keywords), na=False)]
    return article_counts, articles_matching_keywords[['Title', 'Author']]



def list_authors(df):
    authors = df['Author'].str.split(';', expand=True).stack().dropna()
    author_counts = Counter(authors)
    most_common_authors = author_counts.most_common(5)
    return most_common_authors

def generate_html_output(top_keywords, articles_matching_keywords, top_authors):
    html = """
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
    for keyword, count in top_keywords:
        html += f"            <li>{keyword} ({count})</li>\n"
    html += "        <ol/>\n\n"

    html += "<h1>Task 2: Articles Matching Top Keywords</h1>"
    html += f"<p>Total articles matching top keywords: {articles_matching_keywords.shape[0]}</p>\n"
    html += "<table border='1'>\n"
    html += "        <tr><th>Title</th><th>Author</th></tr>\n"
    for title, author in articles_matching_keywords.values:
        html += f"        <tr><td>{title}</td><td>{author}</td></tr>\n"
    html += "    </table>\n\n"

    html += "<h1>Task 3: Authors Discussing Top Keywords</h1>"
    html += "<ol>\n"
    for author, count in top_authors:
        html += f"            <li>{author} ({count})</li>\n"
    html += "        </ol>\n\n"

    html += "</body></html>"
    return html

def write_html_to_file(html, output_path):
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
