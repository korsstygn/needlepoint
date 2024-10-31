### Natural Language Description
Step-by-Step Explanation
Import Libraries:

The script starts by importing necessary Python libraries such as pandas, WordCloud, base64, BytesIO, matplotlib, Counter, and re.
Read Dataset:

It reads a CSV file into a DataFrame using pd.read_csv(). This dataset is assumed to contain information about news articles.
Interactive Keyword Exclusion Process:

The script initializes an empty list removed_keywords and an empty list top_5_keywords.
In an infinite loop, it identifies the top 5 keywords based on their frequency in the DataFrame.
It displays these top 5 keywords along with their frequencies and prompts the user to select which keywords they want to remove. The user can input multiple keyword numbers separated by commas or type 'done' to finish removing keywords.
Keywords marked for removal are added to removed_keywords, and the top 5 keywords list is updated accordingly.
Display All Keywords:

After exiting the loop, it displays all keywords and their frequencies as a single line in natural language format.
Filter Articles Matching Top 5 Keywords:

The script filters the DataFrame to include only articles that match any of the top 5 keywords.
It prints out the titles of these articles along with their indices.
Generate Word Cloud:

A word cloud is generated based on the descriptions of the filtered articles.
The word cloud is saved as an SVG file in the NewsDB-Python/reports/ directory.
Write Results to Markdown File:

The script writes a markdown report containing:
Top 5 keywords and their frequencies.
All keywords and their frequencies.
Articles matching the top 5 keywords, each linked with their permalinks.
A link to the word cloud image.
Output Messages:

The script prints messages indicating where the results have been saved (CSV file and markdown file).
Natural Language Pseudocode
Import necessary libraries
Read dataset from CSV file into DataFrame
Initialize removed_keywords list and top_5_keywords list
While True:
If top_5_keywords is empty, identify top 5 keywords
Split 'Keywords' column by ';', explode to separate keywords, strip whitespace
Get value counts of all keywords
Select top 5 keywords
Else, remove marked keywords from removed_keywords
Display current top keywords and frequencies
Prompt user for input to remove keywords or finish
If 'done', break loop
Otherwise, update removed_keywords and top_5_keywords
Display all keywords and their frequencies
Filter articles matching the top 5 keywords
Generate word cloud based on filtered articles' descriptions
Save word cloud as SVG file
Write results to markdown file:
Create headings for different sections
Display top 5 keywords with frequencies
Display all keywords with frequencies
Group and display articles matching the top 5 keywords
Add link to saved word cloud image
Print messages indicating save locations

### Natural language

### Natural Language Pseudocode

1. **Import necessary libraries**
2. **Read dataset from CSV file into DataFrame**
3. **Initialize `removed_keywords` list and `top_5_keywords` list**
4. **While True:**
   - If `top_5_keywords` is empty, identify top 5 keywords
     - Split 'Keywords' column by ';', explode to separate keywords, strip whitespace
     - Get value counts of all keywords
     - Select top 5 keywords
   - Else, remove marked keywords from `removed_keywords`
   - Display current top keywords and frequencies
   - Prompt user for input to remove keywords or finish
   - If 'done', break loop
   - Otherwise, update `removed_keywords` and `top_5_keywords`
5. **Display all keywords and their frequencies**
6. **Filter articles matching the top 5 keywords**
7. **Generate word cloud based on filtered articles' descriptions**
8. **Save word cloud as SVG file**
9. **Write results to markdown file:**
   - Create headings for different sections
   - Display top 5 keywords with frequencies
   - Display all keywords with frequencies
   - Group and display articles matching the top 5 keywords
   - Add link to saved word cloud image
10. **Print messages indicating save locations**




### Algorithmic Pseudocode

BEGIN
    IMPORT pandas, WordCloud, base64, BytesIO, matplotlib, Counter, re
    
    // Step 2: Read dataset from CSV file into DataFrame
    input_file_path = "NewsDB-Python/datasets/dataset.csv"
    df = pd.read_csv(input_file_path)
    
    removed_keywords = []
    top_5_keywords = []
    
    WHILE True DO
        IF top_5_keywords is empty THEN
            // Step 3: Identify top 5 keywords
            all_keywords = split(df['Keywords'], ';').explode().str.strip()
            keyword_counts = value_counts(all_keywords)
            top_5_keywords = get_top_n_keywords(keyword_counts, 5)
        ELSE
            // Remove marked keywords
            filtered_keywords = [keyword for keyword in keyword_counts.index.tolist() if keyword not in removed_keywords]
            top_5_keywords = get_top_n_keywords(filtered_keywords, 5)
        
        // Step 4: Display current top keywords and frequencies
        display("Current Top Keywords and Their Frequencies:")
        FOR idx, keyword IN enumerate(top_5_keywords) DO
            count = get_count(keyword, keyword_counts)
            status = "[removed by user]" if keyword in removed_keywords else ""
            print(idx + 1, ". ", keyword, ": ", count, status)
        
        // Step 5: Prompt user for input
        user_input = input("Enter the number of the keyword you want to remove (comma-separated if multiple), or 'done' to finish: ")
        IF user_input is "done" THEN
            BREAK
        END IF
        
        TRY
            to_remove = [int(num) - 1 FOR num IN split(user_input, ',')]
            removed_keywords.extend([top_5_keywords[i] FOR i IN to_remove])
            top_5_keywords = [keyword for keyword in top_5_keywords if keyword not in removed_keywords]
        CATCH ValueError THEN
            print("Invalid input. Please enter the number(s) of the keyword you want to remove.")
        
    END WHILE
    
    // Step 6: Display all keywords and their frequencies
    all_keywords_str = ', '.join([f"{keyword}({count})" FOR keyword, count IN keyword_counts.items()])
    print(f"\nAll Keywords and Their Frequencies: {all_keywords_str}")
    
    // Step 7: Filter articles matching the top 5 keywords
    filtered_df = df[df['Keywords'].str.contains('|'.join(top_5_keywords), na=False)]
    display("\nArticles Matching the Top 5 Keywords:")
    FOR idx, row IN enumerate(filtered_df.iterrows()) DO
        print(idx + 1, ". ", row.get('Title', 'No Title'))
    
    // Step 8: Generate word cloud based on filtered articles' descriptions
    descriptions_top_keywords = join(filtered_df['Description'].dropna())
    wordcloud = WordCloud(width=1200, height=960).generate(descriptions_top_keywords)
    plt.figure(figsize=(8, 4))
    imshow(wordcloud, interpolation='bilinear')
    axis('off')
    svg_image = BytesIO()
    savefig(svg_image, format='svg')
    
    encoded_svg = base64.b64encode(svg_image.getvalue()).decode()
    wordcloud_svg = f"<img src='data:image/svg+xml;base64,{encoded_svg}' width='1200' height='960'/>"
    
    // Step 9: Save word cloud as SVG file
    WITH open("NewsDB-Python/reports/Descriptions_word_cloud.svg", "w") AS f DO
        f.write(wordcloud_svg)
    END WITH
    
    display("Word cloud saved to NewsDB-Python/reports/Descriptions_word_cloud.svg")
    
    // Step 10: Write results to markdown file
    md_file_path = "Report.md"
    WITH open(md_file_path, 'w') AS md DO
        write(md, "# Dataset report\n\n")
        write(md, "**Top 5 Keywords and Their Frequencies**\n\n")
        FOR idx, keyword IN enumerate(top_5_keywords) DO
            count = get_count(keyword, keyword_counts)
            write(md, f"{idx + 1}. {keyword} ({count})\n")
        
        write(md, "\n**All Keywords and Their Frequencies**\n\n")
        all_keywords_str_md = ', '.join([f"{keyword}({count})" FOR keyword, count IN keyword_counts.items()])
        write(md, f"{all_keywords_str_md}\n\n")

        write(md, "**Articles Matching the Top 5 Keywords**\n\n")
        
        articles_by_keyword = {}
        
        FOR idx, row IN enumerate(filtered_df.iterrows()) DO
            FOR keyword IN top_5_keywords DO
                IF keyword IN row['Keywords'] THEN
                    IF keyword NOT IN articles_by_keyword THEN
                        articles_by_keyword[keyword] = []
                    END IF
                    article_info = {'title': row.get('Title', 'No Title'), 'permalink': row.get('Permalink', '#')}
                    append(articles_by_keyword[keyword], article_info)
        
        FOR keyword, articles IN articles_by_keyword.items() DO
            write(md, f"\n**{keyword} ({len(articles)})**\n")
            FOR article IN articles DO
                title = article['title']
                permalink = article['permalink']
                write(md, f"1. <a href='{permalink}'>{title}</a>\n")

        write(md, "\n\n**Wordcloud based on the descriptions of the top five articles**\n\n")             
        write(md, f"<img src='NewsDB-Python/reports/Descriptions_word_cloud.svg'>")
    END WITH
    
    display(f"Results saved to {file_path} and {md_file_path}")
END
