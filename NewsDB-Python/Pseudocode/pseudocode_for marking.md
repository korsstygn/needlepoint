1. Read CSV: Load the dataset from the CSV file.
2. Initialize Variables: Create lists to store removed keywords and the top 5 keywords.
3. Keyword Loop: Keep displaying the top 5 keywords until the user decides to stop.
4. Input Handling: Ask the user which keywords to remove, update the list of removed keywords, and refresh the top 5.
5. Generate Keyword String: Create a string of all keywords and their frequencies.
6. Filter Articles: Select articles that match the remaining top 5 keywords.
7. Create Word Cloud: Generate a word cloud based on the descriptions of these articles.
8. Save Word Cloud: Save the word cloud as both an SVG and a PNG file.
9. Write Markdown Report: Write all results to a Markdown file, embedding both the SVG and PNG images.
---
**Natural language Pseudocode**

```Pseudocode
# Load the dataset
read CSV into dataframe df

# Initialize removed keywords and top 5 keywords lists
removed_keywords = []
top_5_keywords = []

# While loop to display top 5 keywords and allow user removal
while True:
    if top_5_keywords is empty:
        all_keywords = explode and clean keywords from df
        keyword_counts = get top 5 keyword counts
        top_5_keywords = keyword_counts indices
    else:
        all_keywords = explode and clean keywords from df
        keyword_counts = get all keyword counts
        top_5_keywords = filter out removed keywords from keyword_counts

    print top 5 keywords and frequencies
    user_input = get user input for keywords to remove or 'done'
    if user_input is 'done':
        break
    else:
        parse user input, update removed_keywords and top_5_keywords

# Create string of all keywords and their frequencies
all_keywords_str = create string from top_5_keywords

# Filter dataframe for articles matching top 5 keywords
filtered_df = filter df based on top_5_keywords

# Generate and save word cloud
descriptions_top_keywords = join descriptions from filtered_df
generate word cloud from descriptions
save word cloud as SVG and PNG

# Write results to markdown file
open markdown file for writing
write dataset report header
write top 5 keywords and their frequencies
write all keywords and their frequencies
write articles matching top 5 keywords
write wordcloud image embedding (SVG with PNG fallback)
```
---
**Algorithmic Pseudocode**

```
ALGORITHM Generate_Report

    INPUT: CSV file path, Markdown file path
    OUTPUT: Markdown report with keywords, articles, and word cloud

    BEGIN
        # Load the dataset
        LOAD CSV INTO dataframe df

        # Initialize variables
        SET removed_keywords TO empty list
        SET top_5_keywords TO empty list

        # Loop for displaying and removing top 5 keywords
        WHILE True DO
            IF top_5_keywords IS empty THEN
                SET all_keywords TO explode and clean keywords from df
                SET keyword_counts TO top 5 keyword counts from all_keywords
                SET top_5_keywords TO indices of keyword_counts
            ELSE
                SET all_keywords TO explode and clean keywords from df
                SET keyword_counts TO all keyword counts from all_keywords
                SET top_5_keywords TO filter out removed keywords from keyword_counts
            
            PRINT top 5 keywords and frequencies

            # Get user input for removing keywords
            SET user_input TO get user input
            IF user_input IS 'done' THEN
                BREAK
            ELSE
                PARSE user_input
                UPDATE removed_keywords and top_5_keywords

        # Create string of all keywords and their frequencies
        SET all_keywords_str TO create string from top_5_keywords

        # Filter dataframe for articles matching top 5 keywords
        SET filtered_df TO filter df based on top_5_keywords

        # Generate and save word cloud
        SET descriptions_top_keywords TO join descriptions from filtered_df
        GENERATE word cloud from descriptions_top_keywords
        SAVE word cloud as SVG and PNG files

        # Write results to markdown file
        OPEN markdown file for writing
        WRITE dataset report header
        WRITE top 5 keywords and their frequencies
        WRITE all keywords and their frequencies
        WRITE articles matching top 5 keywords
        WRITE wordcloud image embedding (SVG with PNG fallback)
    END
```
