import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Read the dataset from CSV
input_file_path = "NewsDB-Python/datasets/dataset.csv"  # Replace with your CSV file path
file_path = "Report.txt"  # Replace with the desired output file path
md_file_path = "Report.md"  # Replace with the desired markdown file path

df = pd.read_csv(input_file_path)

# Interactive keyword exclusion process
removed_keywords = []  # Initialize removed keywords list
top_5_keywords = []

# Task 1: Display top 5 keywords and their frequencies
while True:
    if not top_5_keywords:  # If the top 5 keywords are not yet populated
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts().head(5)
        top_5_keywords = keyword_counts.index.tolist()
    else:  # If we already have top 5 keywords, remove those that the user has marked for removal
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts()
        top_5_keywords = [keyword for keyword in keyword_counts.index.tolist() if keyword not in removed_keywords][:5]

    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, keyword in enumerate(top_5_keywords):
        count = keyword_counts.get(keyword, 0)
        status = "[removed by user]" if keyword in removed_keywords else ""
        print(f"{idx + 1}. {keyword}: {count}")
    
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        removed_keywords.extend([top_5_keywords[i] for i in to_remove])
        top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")

# Task 1: Display all keywords and their frequencies as a single line
all_keywords_str = ', '.join([f"{keyword}({count})" for keyword, count in keyword_counts.items()])
print(f"\nAll Keywords and Their Frequencies: {all_keywords_str}")

# TASK 2: Articles matching the top 5 keywords
filtered_df = df[df['Keywords'].str.contains('|'.join(top_5_keywords), na=False)]
print("\nArticles Matching the Top 5 Keywords:")
for idx, row in filtered_df.iterrows():
    print(f"{idx + 1}. {row.get('Title', 'No Title')}")

# Task 4: Word cloud based on descriptions of articles matching the remaining top 5 keywords
descriptions_top_keywords = ' '.join(filtered_df['Description'].dropna())  # join all descriptions in a single string, dropping NaNs
wordcloud = WordCloud(width=1200, height=960).generate(descriptions_top_keywords)  # generate word cloud with the joined descriptions
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
svg_image = BytesIO()
plt.savefig(svg_image, format='svg')  # Save word cloud as svg image
encoded_svg = base64.b64encode(svg_image.getvalue()).decode()  # Encoding the svg image to display in HTML report
wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>" 
with open("NewsDB-Python/reports/Descriptions_word_cloud.svg", "w") as f:  # Save image
    f.write(wordcloud_svg)
print("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.svg")

# Write the results to a markdown file
with open(md_file_path, 'w') as md:
    md.write("# Dataset report\n\n")    
    md.write("**Top 5 Keywords and Their Frequencies**\n\n")
    for idx, keyword in enumerate(top_5_keywords):
        count = keyword_counts.get(keyword, 0)
        status = "[removed by user]" if keyword in removed_keywords else ""
        md.write(f"{idx + 1}. {keyword} ({count}) {status}\n")

    md.write("\n**All Keywords and Their Frequencies**\n\n")
    all_keywords_str_md = ', '.join([f"{keyword}({count})" for keyword, count in keyword_counts.items()])
    md.write(f"{all_keywords_str_md}\n\n")

    md.write("**Articles Matching the Top 5 Keywords**\n\n")
    articles_by_keyword = {}
    
    # Group articles by keywords
    for idx, row in filtered_df.iterrows():
        for keyword in top_5_keywords:
            if keyword in row['Keywords']:
                if keyword not in articles_by_keyword:
                    articles_by_keyword[keyword] = []
                article_info = {
                    'title': row.get('Title', 'No Title'),
                    'authors': row.get('Author', 'No Author').split(';'),  # Split authors by ';'
                    'permalink': row.get('Permalink', '#')
                }
                articles_by_keyword[keyword].append(article_info)
    
    article_idx = 1
    for keyword, articles in articles_by_keyword.items():
        md.write(f"\n**{keyword} ({len(articles)})**\n")
        for article in articles:
            title = article['title']
            authors = '\n'.join([f"  - {author}" for author in article['authors']])
            permalink = article['permalink']
            md.write(f"{article_idx}. **Authors:** \n{authors}\nTitle: <a href='{permalink}'>{title}</a>\n")
            article_idx += 1

    md.write("\n\n**Wordcloud based on the descriptions of the articles matching the top five keywords**\n\n")             
    md.write(f"<img src='NewsDB-Python/reports/Descriptions_word_cloud.svg'>")    

print(f"Results saved to {file_path} and {md_file_path}")
