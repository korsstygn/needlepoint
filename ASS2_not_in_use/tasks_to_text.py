import pandas as pd
import numpy as np

# Read the dataset from CSV
input_file_path = "NewsDB-Python/datasets/dataset.csv"  # Replace with your CSV file path
file_path = "Report.txt"  # Replace with the desired output file path
df = pd.read_csv(input_file_path)

# Interactive keyword exclusion process
removed_keywords = [] # Initialize removed keywords list
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
        top_5_keywords = [keyword for keyword, count in keyword_counts.items() if keyword not in removed_keywords][:5]
    
    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, keyword in enumerate(top_5_keywords):
        print(f"{idx + 1}. {keyword}")
        # print(all_keywords)        
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        print(top_5_keywords)
        break
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        removed_keywords.extend([top_5_keywords[i] for i in to_remove])
        top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")

def analyze_keywords(df):
    if df is not None:
        report = "\nKeyword Analysis:\n"
        
        # Get unique keywords
        all_keywords = set()
        for index, row in df.iterrows():
            keywords = row['Keywords'].split(';')
            for keyword in keywords:
                all_keywords.add(keyword.strip())
                
        report += f"Total Unique Keywords: {len(all_keywords)}\n"
        report += f"Unique Keywords:\n{', '.join(all_keywords)}\n\n"
        
        # Analyze keywords by author
        keyword_authors = {}
        for index, row in df.iterrows():
            if pd.notnull(row['Author']) and isinstance(row['Author'], str):
                authors = row['Author'].split(';')
            else:
                authors = []
            
            if pd.notnull(row['Keywords']) and isinstance(row['Keywords'], str):
                keywords = row['Keywords'].split(';')
            else:
                keywords = []
            
            for keyword, author in zip(keywords, authors):
                keyword = keyword.strip()
                author = author.strip()
                if keyword not in keyword_authors:
                    keyword_authors[keyword] = []
                keyword_authors[keyword].append(author)
        
        report += "Keyword by Author:\n"
        for keyword, authors in keyword_authors.items():
            report += f"{keyword}: {', '.join(list(set(authors)))}\n"
        
        # Analyze keywords by title
        keyword_titles = {}
        for index, row in df.iterrows():
            if pd.notnull(row['Title']) and isinstance(row['Title'], str):
                titles = row['Title'].split(';')
            else:
                titles = []
            
            if pd.notnull(row['Keywords']) and isinstance(row['Keywords'], str):
                keywords = row['Keywords'].split(';')
            else:
                keywords = []
            
            for keyword, title in zip(keywords, titles):
                keyword = keyword.strip()
                title = title.strip()
                if keyword not in keyword_titles:
                    keyword_titles[keyword] = []
                keyword_titles[keyword].append(title)
        
        report += "\nKeyword by Title:\n"
        for keyword, titles in keyword_titles.items():
            report += f"{keyword}: {', '.join(list(set(titles)))}\n"
    
    else:
        report = "No DataFrame to analyze."
    
    return report

# Function to save the analysis report to a text file
def save_report(report, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(report)
        print("Report saved successfully.")
    except Exception as e:
        print(f"Error saving report: {e}")

# Main function
def main():
    input_file_path = "NewsDB-Python/datasets/dataset.csv"  # Replace with your CSV file path
    output_file_path = "keyWords_report.txt"  # Replace with the desired output file path
    
    if df is not None:
        report = analyze_keywords(df)
        save_report(report, output_file_path)

if __name__ == "__main__":
    main()
