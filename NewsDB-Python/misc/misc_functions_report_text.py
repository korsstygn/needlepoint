import pandas as pd
import numpy as np

# Function to read the CSV file
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Function to perform basic analysis on the DataFrame
def analyze_data(df):
    if df is not None:
        report = "\nBasic Data Analysis:\n"
        
        # Display the first few rows of the DataFrame
        report += f"First 5 rows:\n{df.head()}\n"
        
        # Display the last few rows of the DataFrame
        report += f"\nLast 5 rows:\n{df.tail()}\n"
        
        # Get the shape of the DataFrame (rows, columns)
        report += f"\nShape: {df.shape}\n"
        
        # Get the information about each column
        report += "\nInformation about each column:\n"
        report += str(df.info()) + "\n"
        
        # Get descriptive statistics for numeric columns
        report += "\nDescriptive statistics:\n"
        report += str(df.describe()) + "\n"
        
        # Check for missing values
        report += "\nMissing Values:\n"
        report += str(df.isnull().sum()) + "\n"
        
        # Get the value counts of categorical columns
        report += "\nValue Counts of Categorical Columns:\n"
        for column in df.select_dtypes(include=['object']).columns:
            report += f"\n{column}:\n{df[column].value_counts(dropna=False)}\n"
    
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
    output_file_path = "report.txt"  # Replace with the desired output file path
    
    df = load_csv(input_file_path)
    if df is not None:
        report = analyze_data(df)
        save_report(report, output_file_path)

if __name__ == "__main__":
    main()
