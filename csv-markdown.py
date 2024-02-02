import pandas as pd

def csv_to_markdown(csv_file_path):
    # Load the CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Remove line breaks from all columns
    df = df.replace('\n', ' ', regex=True)

    # Replace blank values with "N/A"
    df = df.fillna("N/A")

    # Create the header row for the Markdown table
    header = '| ' + ' | '.join(df.columns) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(df.columns)) + ' |'
    
    # Create the rows for the Markdown table
    rows = []
    for _, row in df.iterrows():
        row_str = '| ' + ' | '.join(map(str, row)) + ' |'
        rows.append(row_str)
    
    # Combine all parts into the Markdown table
    markdown_table = '\n'.join([header, separator] + rows)
    
    return markdown_table

def main():
    # Prompt the user to enter the path of the CSV file
    csv_file_path = input("Enter the path of the CSV file: ")

    # Check if the user canceled the input
    if not csv_file_path:
        print("File selection canceled.")
    else:
        # Specify the output file path
        output_file_path = 'Markdown.txt'

        # Call the function to generate the Markdown table
        markdown_table = csv_to_markdown(csv_file_path)

        # Write the Markdown table to the output file
        with open(output_file_path, 'w') as f:
            f.write(markdown_table)

        print(f"Markdown table saved to {output_file_path}")

if __name__ == "__main__":
    main()
