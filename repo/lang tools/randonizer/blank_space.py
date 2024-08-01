def filter_csv_by_length(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        csv_data = file.readlines()

    filtered_lines = [line.strip() for line in csv_data if len(line.strip()) >= 4]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(filtered_lines))


# Example usage:
csv_file_path = "randonizer\\bl_input_1.csv"  # Replace with your CSV file path
filter_csv_by_length(csv_file_path)
