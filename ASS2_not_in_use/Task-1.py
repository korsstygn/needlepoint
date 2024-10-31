import pandas as pd

# Read the dataset from CSV
input_file_path = "NewsDB-Python/datasets/dataset.csv"  # Replace with your CSV file path
file_path = "Report.txt"  # Replace with the desired output file path
md_file_path = "Report.md"  # Replace with the desired markdown file path

df = pd.read_csv(input_file_path)

# Interactive keyword exclusion process
removed_keywords = []  # Initialize removed keywords list
top_5_keywords = []

# Task 1: Display top 5 keywords and their frequencies
while True:
    if not top_5_keywords:  # If the top 5 keywords are not yet populated
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts().head(5)
        top_5_keywords = keyword_counts.index.tolist()
    else:  # If we already have top 5 keywords, remove those that the user has marked for removal
        all_keywords = df['Keywords'].str.split(';').explode().str.strip()
        keyword_counts = all_keywords.value_counts()
        top_5_keywords = [keyword for keyword in keyword_counts.index.tolist() if keyword not in removed_keywords][:5]

    print("\nCurrent Top Keywords and Their Frequencies:")
    for idx, keyword in enumerate(top_5_keywords):
        count = keyword_counts.get(keyword, 0)
        # status = "[removed by user]" if keyword in removed_keywords else ""
        print(f"{idx + 1}. {keyword}: {count}")
    
    user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    try:
        to_remove = [int(num) - 1 for num in user_input.split(',')]
        removed_keywords.extend([top_5_keywords[i] for i in to_remove])
        top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
    except ValueError:
        print("Invalid input. Please enter the number(s) of the keyword you want to remove.")

# Task 1: Display all keywords and their frequencies
all_keyword_counts = df['Keywords'].str.split(';').explode().str.strip().value_counts()
print("\nAll Keywords and Their Frequencies:")
for keyword, count in all_keyword_counts.items():
    status = "[removed by user]" if keyword in removed_keywords else ""
    # print(f"{keyword}: {count} {status}")

# Write the results to a text file
with open(file_path, 'w') as f:
    f.write("Top 5 Keywords and Their Frequencies:\n")
    for idx, keyword in enumerate(top_5_keywords):
        count = keyword_counts.get(keyword, 0)
        status = "[removed by user]" if keyword in removed_keywords else ""
        f.write(f"{idx + 1}. {keyword}: {count} {status}\n")

    f.write("\nAll Keywords and Their Frequencies:\n")
    for keyword, count in all_keyword_counts.items():
        status = "[removed by user]" if keyword in removed_keywords else ""
        f.write(f"{keyword}: {count} {status}\n")

# Write the results to a markdown file
with open(md_file_path, 'w') as md:
    md.write("# Top 5 Keywords and Their Frequencies\n")
    for idx, keyword in enumerate(top_5_keywords):
        count = keyword_counts.get(keyword, 0)
        md.write(f"{idx + 1}. {keyword} ({count})\n")

    md.write("\n## All Keywords and Their Frequencies\n")
    md.write("\n".join([f"- {keyword} ({count}) {('[**removed by user**]' if keyword in removed_keywords else '')}" for keyword, count in all_keyword_counts.items()]))

print(f"Results saved to {file_path} and {md_file_path}")
