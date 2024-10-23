import pandas as pd  # Import the pandas library for data manipulation and analysis.
from wordcloud import WordCloud  # Import the WordCloud class from the wordcloud library to create word clouds.

# Optionally, if you want to use matplotlib for plotting:
# import matplotlib.pyplot as plt

# Optionally, if you prefer using Plotly for interactive plots:
# import plotly.graph_objs as go

import jinja2  # Import the Jinja2 templating engine to generate HTML files dynamically.
from base64 import b64encode  # Import the b64encode function from the base64 module to encode SVG data.

selected_columns = []  # Initialize an empty list to store the selected columns for word cloud visualization.

# Define a function to read a CSV file and create word clouds for selected columns.
def create_word_clouds(file_path):
    # Read the CSV file into a DataFrame using pandas.
    df = pd.read_csv(file_path)
    
    # List all available column names in the DataFrame and print them with their indices.
    column_names = df.columns.tolist()
    print("Available columns:")
    for idx, column in enumerate(column_names):
        print(f"{idx + 1}: {column}")
    

    while True:
        try:
            # Prompt the user to enter the indices of columns they want to visualize as word clouds.
            choice = input("Enter the indices of the columns you want to visualize as word clouds (comma-separated): ").split(',')
            selected_indices = [int(i.strip()) for i in choice]
            
            # Check if the entered indices are valid and within the range of available columns.
            if all(0 < idx <= len(column_names) for idx in selected_indices):
                selected_columns = [column_names[idx - 1] for idx in selected_indices]
                break
            else:
                print("Invalid indices. Please enter valid indices separated by commas.")
        except ValueError:
            # Handle cases where the user enters invalid input (e.g., non-integer).
            print("Invalid input. Please enter comma-separated integers.")
    
    # Create word clouds for each selected column.
    for column in selected_columns:
        text = ' '.join(df[column].dropna().astype(str))
        
        # Skip columns that have no valid text data.
        if not text.strip():
            continue
        
        # Generate a WordCloud object with specified width, height, and background color.
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Save the word cloud as an HTML file using base64 encoding for SVG data.
        html_filename = f"{column.replace(' ', '_')}_word_cloud.html"
        with open(html_filename, 'w') as f:
            f.write('<img src="data:image/svg+xml;base64,' + b64encode(wordcloud.to_svg().encode()).decode() + '" width="800" height="400"/>')
        print(f"Saved {html_filename}")
        
    
    # Create an index.html file with links to the word cloud pages using a Jinja2 template.
    template_loader = jinja2.FileSystemLoader(searchpath=".")  # Set up the Jinja2 template loader.
    template_env = jinja2.Environment(loader=template_loader)  # Create a Jinja2 environment.
    template = template_env.get_template("index_template.html")  # Load the index_template.html template.
    output = template.render(columns=[f"{col.replace(' ', '_')}_word_cloud.html" for col in selected_columns])  # Render the template with word cloud filenames.
    
    with open("index.html", "w") as f:
        f.write(output)  # Write the rendered HTML content to index.html.
    print("Created index.html with word cloud links.")

# Specify the path to your CSV file.
file_path = 'dataset.csv'

# Call the function to read the CSV file and create word clouds for selected columns, then generate HTML files.
create_word_clouds(file_path)

# Display the selected columns and their corresponding word cloud files.
selected_columns = [f"{col.replace(' ', '_')}_word_cloud.html" for col in selected_columns]
print("Selected word clouds:")
for column in selected_columns:
    print(column)
