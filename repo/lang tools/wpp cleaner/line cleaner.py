import csv

def process_csv(input_file, output_file, chars_to_remove):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    processed_lines = []
    for line in lines:
        # Find where the text starts after the timestamp
        start_index = line.find('] ') + 2
        # Remove specified number of characters from the beginning
        processed_line = line[start_index + chars_to_remove:].strip()
        # Prepend '[' to the processed line
        processed_line = '[' + processed_line
        processed_lines.append(processed_line)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in processed_lines:
            writer.writerow([line])

# Example usage:
input_file = r'C:\\Users\\Ivan Bolivar\\Desktop\\python1\\back up\\lang tools\\wpp cleaner\\input_wpp.csv'
output_file = r'C:\Users\\Ivan Bolivar\\Desktop\\python1\\back up\\lang tools\\wpp cleaner\\wpp_output.csv'
characters_to_remove = 8  # Adjust this number based on your specific requirement

process_csv(input_file, output_file, characters_to_remove)
