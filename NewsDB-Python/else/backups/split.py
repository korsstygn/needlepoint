import pandas as pd

# Function to read the CSV file and handle multi-entry columns
def split_multi_entries(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Identify columns with multiple entries separated by semicolons
    multi_entry_columns = [col for col in df.columns if any(df[col].astype(str).str.contains(';'))]
    
    # Print the original column names where semicolons were found
    print("Columns with multiple entries separated by semicolons:")
    for column in multi_entry_columns:
        print(column)
    
    # Create new rows for each split value and save them to separate CSV files
    for multi_entry_column in multi_entry_columns:
        original_column_name = multi_entry_column  # Use the column name directly
        output_file_path = f"{original_column_name}_split.csv"
        
        # Explode the DataFrame
        df_exploded = df.explode(multi_entry_column)
        
        # Save the new DataFrame to a CSV file
        df_exploded.to_csv(output_file_path, index=False)
        print(f"Saved {output_file_path}")  # Print the path to the splitted file

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to handle multi-entry columns and present statistics
split_multi_entries(file_path)

# Display the DataFrame after handling multi-entry columns
print("Individual split columns saved successfully.")
