### Natural Language Description
1. **Initialize Data and Variables:**
   - Read the dataset from a CSV file named `dataset.csv`.
   - Create lists to store removed keywords and top 5 keywords.

2. **Interactive Keyword Exclusion Process:**
   - Populate the top 5 keywords based on frequency in the dataset.
   - Allow user to remove specific keywords interactively through a loop until they indicate completion.

3. **Filter Articles by Top Keywords:**
   - Use the remaining top 5 keywords to filter articles from the dataset.

4. **Identify Authors and Articles:**
   - For each article, check if it contains any of the top 5 keywords.
   - Store relevant information (keyword, author, title, permalink, and description) in a list.
   - Remove duplicates from the list to ensure unique entries.

5. **Generate Word Cloud:**
   - Join all descriptions from the filtered articles into a single string.
   - Generate a word cloud based on this combined text.
   - Save the word cloud as an SVG and encode it for HTML display.

6. **Generate Output Files:**
   - Create a Markdown file to summarize the keyword analysis and list articles.
   - Generate an HTML report that includes sections for top keywords, relevant articles, authors discussing the keywords, and the word cloud.

### Algorithmic Pseudocode

```pseudocode
# Initialize Data and Variables
1. Read dataset from 'NewsDB-Python/datasets/dataset.csv' into a DataFrame df
2. Initialize removed_keywords as an empty list
3. Initialize top_5_keywords as an empty list

# Interactive Keyword Exclusion Process
4. Populate top_5_keywords with the top 5 most frequent keywords in df['Keywords']
5. While True:
6.   Display top_5_keywords and their frequencies
7.   user_input = input("Enter the number of the keyword to remove, or 'done' to finish: ")
8.   If user_input == 'done':
9.     break
10.    try:
11.      to_remove = [int(num) - 1 for num in user_input.split(',')]
12.      removed_keywords.extend([top_5_keywords[i] for i in to_remove])
13.      top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]

# Filter Articles by Top Keywords
14. keywords_set = set(top_5_keywords)  # Use the remaining top 5 keywords
15. articles_top_keywords = df[df['Keywords'].apply(lambda x: any(keyword in x for keyword in keywords_set))]
16. Print the number of articles matching top 5 keywords: len(articles_top_keywords)

# Identify Authors and Articles
17. Initialize author_articles as an empty list
18. For each row in df:
19.   For each keyword in top_5_keywords:
20.     If keyword is in row['Keywords']:
21.       Append {'Keyword': keyword, 'Author': row['Author'], 'Title': row['Title'], 'Permalink': row['Permalink'], 'Description': row['Description']} to author_articles
22. Remove duplicates from author_articles

# Generate Word Cloud
23. descriptions_top_keywords = ' '.join(articles_top_keywords['Description'].dropna())
24. Generate word cloud from descriptions_top_keywords and save as SVG
25. Encode the SVG for HTML display
26. Save word cloud in 'NewsDB-Python/reports/Descriptions_word_cloud.html'

# Generate Output Files
27. Create Markdown file to summarize keyword analysis and list articles
28. Initialize report_md as a string
29. For each keyword in top_5_keywords:
30.   Append f". {keyword}\n\n" to report_md
31. For each row in articles_top_keywords:
32.   Append f"- #### Title: <a href='{row['Permalink']}'>{row['Title']}</a>\n" to report_md
33.   Append f"**Author**: {row['Author']}\n" to report_md
34.   Append f"**|** **Description**: {row['Description']}\n\n" to report_md
35. For each article in author_articles:
36.   Append f"- **Keyword**: {article['Keyword']}\n" to report_md
37.   Append f"  - **Author**: {article['Author']}\n" to report_md
38.   Append f"  - **Title**: <a href='{article['Permalink']}'>{article['Title']}</a>\n" to report_md
39.   Append f"  - **Description**: {article['Description']}\n\n" to report_md
40. Append f"TASK 4: Word cloud based on descriptions of all articles matching the keywords\n![image](NewsDB-Python/reports/Descriptions_word_cloud.svg)\n" to report_md
41. Write report_md to 'NewsDB-Python/reports/keyword_analysis_report.md'
42. Save HTML report to 'NewsDB-Python/reports/report.html'