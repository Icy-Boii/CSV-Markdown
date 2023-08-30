import pandas as pd

def csv_to_markdown(csv_file):
    # Load the CSV file using pandas
    df = pd.read_csv(csv_file)
    
    # Create the header row for the Markdown table
    header = '| ' + ' | '.join(df.columns) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(df.columns)) + ' |'
    
    # Create the rows for the Markdown table
    rows = []
    for index, row in df.iterrows():
        row_str = '| ' + ' | '.join([str(val) for val in row]) + ' |'
        rows.append(row_str)
    
    # Combine all parts into the Markdown table
    markdown_table = '\n'.join([header, separator] + rows)
    
    return markdown_table

# Prompt the user to enter the path of the CSV file
csv_file_path = input("Enter the path of the CSV file: ")

# Specify the output file path
output_file_path = 'Markdown.txt'

# Call the function to generate the Markdown table
markdown_table = csv_to_markdown(csv_file_path)

# Write the Markdown table to the output file
with open(output_file_path, 'w') as f:
    f.write(markdown_table)

print(f"Markdown table saved to {output_file_path}")
