import pandas as pd

# Function to read the CSV file and present statistics
def csv_statistics(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Display the first few rows of the DataFrame
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Display basic information about the DataFrame
    print("\nBasic Information:")
    print(df.info())
    
    # Display the shape of the DataFrame (number of rows and columns)
    print("\nShape of the dataset:")
    print(df.shape)
    
    # Display descriptive statistics of the DataFrame (e.g., mean, min, max, etc.)
    print("\nDescriptive Statistics:")
    print(df.describe())
    
    # Display the number of unique values in each column
    print("\nNumber of Unique Values in Each Column:")
    unique_counts = df.nunique()
    print(unique_counts)
    
    # Display the number of missing values in each column
    print("\nNumber of Missing Values in Each Column:")
    missing_values = df.isnull().sum()
    print(missing_values)
    
# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to present statistics
csv_statistics(file_path)
