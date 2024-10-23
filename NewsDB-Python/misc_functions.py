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
        print("\nBasic Data Analysis:")
        
        # Display the first few rows of the DataFrame
        print("First 5 rows:\n", df.head())
        
        # Display the last few rows of the DataFrame
        print("\nLast 5 rows:\n", df.tail())
        
        # Get the shape of the DataFrame (rows, columns)
        print(f"\nShape: {df.shape}")
        
        # Get the information about each column
        print("\nInformation about each column:")
        print(df.info())
        
        # Get descriptive statistics for numeric columns
        print("\nDescriptive statistics:\n", df.describe())
        
        # Check for missing values
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        # Get the value counts of categorical columns
        print("\nValue Counts of Categorical Columns:")
        for column in df.select_dtypes(include=['object']).columns:
            print(f"\n{column}:\n", df[column].value_counts(dropna=False))
    
    else:
        print("No DataFrame to analyze.")

# Main function
def main():
    file_path = "dataset.csv"  # Replace with your CSV file path
    df = load_csv(file_path)
    if df is not None:
        analyze_data(df)

if __name__ == "__main__":
    main()
