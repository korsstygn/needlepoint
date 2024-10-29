import pandas as pd
from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import plotly.graph_objs as go
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
        
    
    # Create an index.html file with links to the word cloud pages
    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index_template.html")
    output = template.render(columns=[f"{col.replace(' ', '_')}_word_cloud.html" for col in selected_columns])
    
    with open("index.html", "w") as f:
        f.write(output)
    print("Created index.html with word cloud links.")

# Specify the path to your CSV file
file_path = 'dataset.csv'

# Call the function to create word clouds and generate HTML files
create_word_clouds(file_path)

# Display the selected columns and their corresponding word cloud files
selected_columns = [f"{col.replace(' ', '_')}_word_cloud.html" for col in selected_columns]
print("Selected word clouds:")
for column in selected_columns:
    print(column)
