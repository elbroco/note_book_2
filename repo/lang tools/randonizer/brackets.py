def add_brackets_to_csv_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        csv_data = file.readlines()

    csv_data_with_brackets = ["[" + line.strip() for line in csv_data]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(csv_data_with_brackets))


# Example usage:
csv_file_path = "randonizer\\bl_input_1.csv"  # Replace with your CSV file path
add_brackets_to_csv_file(csv_file_path)
