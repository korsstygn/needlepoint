import pandas as pd
from collections import Counter

sorted_keywords = []

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
        
        # Get unique keywords and their frequency of use across titles and authors
        all_keywords = []
        keyword_articles = {}  # To store permalinks of articles using each keyword
        for index, row in df.iterrows():
            if pd.notnull(row['Keywords']) and isinstance(row['Keywords'], str):
                keywords = row['Keywords'].split(';')
                for keyword in keywords:
                    keyword = keyword.strip()
                    all_keywords.append(keyword)
                    if keyword not in keyword_articles:
                        keyword_articles[keyword] = []
                    permalink = row['Permalink']  # Use the Permalink from the same row
                    keyword_articles[keyword].append(permalink)
        
        # Count the frequency of each keyword
        keyword_counts = Counter(all_keywords)
        
        # Generate the report based on frequency of use
        global sorted_keywords  # Declare as global to modify the outer scope variable
        sorted_keywords = keyword_counts.most_common()
        
        report += f"Total Unique Keywords: {len(sorted_keywords)}\n"
        report += "\nKeywords by Frequency:\n"
        for keyword, count in sorted_keywords:
            report += f"{keyword} ({count}): "
            if keyword in keyword_articles:
                report += ", ".join(keyword_articles[keyword]) + "\n"
            else:
                report += "No articles\n"
        
        # Prepare data for CSV generation
        keyword_data = []
        for keyword, count in sorted_keywords:
            articles = keyword_articles.get(keyword, [])
            for article in articles:
                description = df[df['Permalink'] == article]['Description'].values if 'Description' in df and pd.notnull(df['Description']) else "No description available"
                if not description.empty:  # Check if the Series is not empty
                    keyword_data.append({
                        'Keyword': keyword,
                        'Frequency': count,
                        'Author': df[df['Permalink'] == article]['Author'].values[0] if 'Author' in df else "Unknown",
                        'Title': df[df['Permalink'] == article]['Title'].values[0],
                        'Permalink': article,
                        'Description': description.iloc[0] if len(description) > 0 else "No description available"
                    })
        
        # Create a DataFrame from the keyword data
        df_report = pd.DataFrame(keyword_data)
        
        # Save the DataFrame to a CSV file
        df_report.to_csv("KW_FREQ_report.csv", index=False)
        print("Report saved successfully to CSV file.")
    
    else:
        report = "No DataFrame to analyze."
    
    return report

# Function to save the analysis report to a text file and CSV file
def save_report(report, csv_file_path, txt_file_path):
    try:
        with open(txt_file_path, 'w') as txt_file:
            txt_file.write(report)
        print("Report saved successfully to text file.")
    except Exception as e:
        print(f"Error saving report: {e}")

# Main function
def main():
    input_file_path = "NewsDB-Python/datatsets/dataset.csv"  # Replace with your CSV file path
    output_file_path = "KW_FREQ_report.csv"  # Replace with the desired output CSV file path
    txt_output_file_path = "KW_FREQ_report.txt"  # Replace with the desired output text file path
    
    df = load_csv(input_file_path)
    if df is not None:
        report = analyze_keywords(df)
        save_report(report, output_file_path, txt_output_file_path)

if __name__ == "__main__":
    main()
