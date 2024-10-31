import pandas as pd

# Function to read the CSV file
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Function to perform basic analysis on specific columns (Author, Title, and Keywords)
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
    
    df = load_csv(input_file_path)
    if df is not None:
        report = analyze_keywords(df)
        save_report(report, output_file_path)

if __name__ == "__main__":
    main()
