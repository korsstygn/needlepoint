import pandas as pd
import numpy as np

# Global variable to store multi-entry columns
multi_entry_columns = []

# Function to read the CSV file and handle multi-entry columns
def split_multi_entries(file_path):
    global multi_entry_columns  # Declare as a global variable
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Identify columns with multiple entries separated by semicolons
    multi_entry_columns = df.apply(lambda x: isinstance(x, str) and ';' in x).index[df.apply(lambda x: isinstance(x, str) and ';' in x).values]
    
    # Print the original column names where semicolons were found
    print("Columns with multiple entries separated by semicolons:")
    for column in multi_entry_columns:
        print(column)

    # Split the multi-entry columns into new columns
    for column in multi_entry_columns:
        # Ensure the column is treated as a string before splitting
        df[column] = df[column].astype(str)
        # Split the multi-entry column into new columns
        df[column] = df[column].str.split(';')
        # Explode the split column into separate rows
        df = df.explode(column)
        # Create new columns for each distinct value in the multi-entry column
        unique_values = df[column].dropna().unique()  # Drop NA values before getting unique values
        for i, value in enumerate(unique_values):
            new_column_name = f"{column}_{i+1}"
            df[new_column_name] = np.where(df[column] == value, value, None)
        # Drop the original multi-entry column
        df = df.drop(columns=[column])
    
    return df

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to handle multi-entry columns and present statistics
df_with_splits = split_multi_entries(file_path)

# Save each modified column to a new CSV file with the original column name as part of the filename
for multi_entry_column in multi_entry_columns:  # This should work now
    original_column_name = multi_entry_column  # Use the column name directly
    output_file_path = f"{original_column_name}_split.csv"
    df_with_splits.to_csv(f"{original_column_name}_split.csv", index=False)

# Display the DataFrame after handling multi-entry columns
print("DataFrame and individual split columns saved successfully.")




# Works but generates ginourmous Files




import pandas as pd
import numpy as np

# Function to read the CSV file and handle multi-entry columns
def split_multi_entries(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Identify columns with multiple entries separated by semicolons
    multi_entry_columns = df.apply(lambda x: isinstance(x, str) and ';' in x).index[df.apply(lambda x: isinstance(x, str) and ';' in x).values]
    
    # Print the original column names where semicolons were found
    print("Columns with multiple entries separated by semicolons:")
    for column in multi_entry_columns:
        print(column)
    
    # Split the multi-entry columns into new columns
    for column in multi_entry_columns:
        # Ensure the column is treated as a string before splitting
        df[column] = df[column].astype(str)
        # Split the multi-entry column into new columns
        df[column] = df[column].str.split(';')
        # Explode the split column into separate rows
        df = df.explode(column)
        # Create new columns for each distinct value in the multi-entry column
        unique_values = df[column].dropna().unique()  # Drop NA values before getting unique values
        for i, value in enumerate(unique_values):
            new_column_name = f"{column}_{i+1}"
            df[new_column_name] = np.where(df[column] == value, value, None)
        # Drop the original multi-entry column
        df = df.drop(columns=[column])
    
    return df, multi_entry_columns  # Return both the DataFrame and the list of columns

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to handle multi-entry columns and present statisticsimport pandas as pd
import numpy as np

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
    
    # Split the multi-entry columns into new columns
    for column in multi_entry_columns:
        # Ensure the column is treated as a string before splitting
        df[column] = df[column].astype(str)
        # Split the multi-entry column into new columns
        df[column] = df[column].str.split(';')
        # Explode the split column into separate rows
        df = df.explode(column)
    
    return df, multi_entry_columns  # Return both the DataFrame and the list of columns

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to handle multi-entry columns and present statistics
df_with_splits, me_columns = split_multi_entries(file_path)

# Save each modified column to a new CSV file with the original column name as part of the filename
for multi_entry_column in me_columns:  # Use the returned list of columns
    original_column_name = multi_entry_column  # Use the column name directly
    output_file_path = f"{original_column_name}_split.csv"
    df_with_splits.to_csv(output_file_path, index=False)
    print(f"Saved {output_file_path}")  # Print the path to the splitted file

# Display the DataFrame after handling multi-entry columns
print("DataFrame and individual split columns saved successfully.")

df_with_splits, me_columns = split_multi_entries(file_path)

# Save each modified column to a new CSV file with the original column name as part of the filename
for multi_entry_column in me_columns:  # Use the returned list of columns
    original_column_name = multi_entry_column  # Use the column name directly
    output_file_path = f"{original_column_name}_split.csv"
    df_with_splits.to_csv(output_file_path, index=False)
    print(f"Saved {output_file_path}")  # Print the path to the splitted file

# Display the DataFrame after handling multi-entry columns
print("DataFrame and individual split columns saved successfully.")


# WORKS but genarates duplicate entries



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
    
    # Split the multi-entry columns into new columns
    for column in multi_entry_columns:
        # Ensure the column is treated as a string before splitting
        df[column] = df[column].astype(str)
        # Split the multi-entry column into new columns
        df[column] = df[column].str.split(';')
        # Explode the split column into separate rows
        df = df.explode(column)
    
    return df, multi_entry_columns  # Return both the DataFrame and the list of columns

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to handle multi-entry columns and present statistics
df_with_splits, me_columns = split_multi_entries(file_path)

# Save each modified column to a new CSV file with the original column name as part of the filename
for multi_entry_column in me_columns:  # Use the returned list of columns
    original_column_name = multi_entry_column  # Use the column name directly
    output_file_path = f"{original_column_name}_split.csv"
    df_with_splits[[multi_entry_column]].to_csv(output_file_path, index=False)
    print(f"Saved {output_file_path}")  # Print the path to the splitted file

# Display the DataFrame after handling multi-entry columns
print("Individual split columns saved successfully.")


# WORDCLOUD WORKING

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import jinja2
from base64 import b64encode
selected_columns =[]

# Function to read the CSV file and create word clouds for selected columns
def create_word_clouds(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # List available columns
    column_names = df.columns.tolist()
    print("Available columns:")
    for idx, column in enumerate(column_names):
        print(f"{idx + 1}: {column}")
    
    selected_columns = []
    while True:
        try:
            choice = input("Enter the indices of the columns you want to visualize as word clouds (comma-separated): ").split(',')
            selected_indices = [int(i.strip()) for i in choice]
            if all(0 < idx <= len(column_names) for idx in selected_indices):
                selected_columns = [column_names[idx - 1] for idx in selected_indices]
                break
            else:
                print("Invalid indices. Please enter valid indices separated by commas.")
        except ValueError:
            print("Invalid input. Please enter comma-separated integers.")
    
    # Create word clouds for selected columns
    for column in selected_columns:
        text = ' '.join(df[column].dropna().astype(str))
        if not text.strip():
            continue  # Skip empty or invalid text
        
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Save the word cloud as an image file
        html_filename = f"{column.replace(' ', '_')}_word_cloud.html"
        with open(html_filename, 'w') as f:
            f.write('<img src="data:image/svg+xml;base64,' + b64encode(wordcloud.to_svg().encode()).decode() + '" width="800" height="400"/>')
        print(f"Saved {html_filename}")
        
        # Create a Plotly graph for the word cloud
        plotly_fig = go.Figure(data=[go.Scatter(x=[], y=[])])
        plotly_fig.update_layout(
            title=f"Word Cloud - {column}",
            annotations=[
                dict(
                    text=open(html_filename, 'r').read(),
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.5, y=0.5,
                    font=dict(size=14)
                )
            ]
        )
        
        plotly_filename = f"{column.replace(' ', '_')}_word_cloud_plot.html"
        plotly_fig.write_html(plotly_filename)
        print(f"Saved {plotly_filename}")
    
    # Create an index.html file with links to the word cloud pages
    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index_template.html")
    output = template.render(columns=[f"{col.replace(' ', '_')}_word_cloud_plot.html" for col in selected_columns])
    
    with open("index.html", "w") as f:
        f.write(output)
    print("Created index.html with word cloud links.")

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to create word clouds and generate HTML files
create_word_clouds(file_path)

# Display the selected columns and their corresponding word cloud files
selected_columns = [f"{col.replace(' ', '_')}_word_cloud_plot.html" for col in selected_columns]
print("Selected word clouds:")
for column in selected_columns:
    print(column)
