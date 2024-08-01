import csv
import random


def shuffle_csv_phrases(input_csv, output_csv):
    # Read the CSV file into a list
    with open(input_csv, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        phrases = list(reader)

    # Shuffle the list of phrases randomly
    random.shuffle(phrases)

    # Write the shuffled list to a new CSV file
    with open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(phrases)


# Example usage
input_csv_file = "randonizer/bl_output_1.csv"
output_csv_file = "randonizer/lines_output.csv"

shuffle_csv_phrases(input_csv_file, output_csv_file)
