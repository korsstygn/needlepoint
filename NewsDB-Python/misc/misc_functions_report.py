import pandas as pd
from jinja2 import Environment, FileSystemLoader

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
        # Display the first few rows of the DataFrame
        first_5_rows = df.head().to_html(index=False)
        
        # Display the last few rows of the DataFrame
        last_5_rows = df.tail().to_html(index=False)
        
        # Get the shape of the DataFrame (rows, columns)
        shape = f"Rows: {df.shape[0]}, Columns: {df.shape[1]}"
        
        # Get the information about each column
        info = df.info()
        
        # Get descriptive statistics for numeric columns
        descriptive_stats = df.describe().to_html(classes='stats-table')
        
        # Check for missing values
        missing_values = df.isnull().sum().to_html(classes='missing-values-table')
        
        # Get the value counts of categorical columns
        value_counts = {}
        for column in df.select_dtypes(include=['object']).columns:
            value_counts[column] = df[column].value_counts(dropna=False).to_html()
        
        return {
            "first_5_rows": first_5_rows,
            "last_5_rows": last_5_rows,
            "shape": shape,
            "info": info,
            "descriptive_stats": descriptive_stats,
            "missing_values": missing_values,
            "value_counts": value_counts
        }
    else:
        return None

# Function to generate HTML report
def generate_html_report(data, output_path):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report.html')
    
    html_content = template.render(data=data)
    
    with open(output_path, 'w') as f:
        f.write(html_content)
    print(f"HTML report generated at {output_path}")

# Main function
def main():
    file_path = "NewsDB-Python/datasets/dataset.csv"  # Replace with your CSV file path
    output_path = "analysis_report.html"  # Specify the output HTML file path
    
    df = load_csv(file_path)
    if df is not None:
        data = analyze_data(df)
        generate_html_report(data, output_path)

if __name__ == "__main__":
    main()
