import csv


def aggregate_lines(input_csv, output_csv):
    with open(input_csv, "r", encoding="utf-8") as file:  # Specify encoding as UTF-8
        reader = csv.reader(file)
        rows = list(reader)

    output_data = []
    current_group = []

    for row in rows:
        for item in row:
            # Check if "[" exists in the item
            if "[" in item:
                if current_group:
                    output_data.append(current_group)
                current_group = []
            current_group.append(item)

    # Append the last group if any
    if current_group:
        output_data.append(current_group)

    # Write the aggregated data to the output CSV
    with open(
        output_csv, "w", newline="", encoding="utf-8"
    ) as file:  # Specify encoding as UTF-8
        writer = csv.writer(file)
        writer.writerows(output_data)


# Example usage
input_csv_file = "randonizer\\bl_input_1.csv"
output_csv_file = "randonizer\\bl_output_1.csv"
aggregate_lines(input_csv_file, output_csv_file)
