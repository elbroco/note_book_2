import random
import csv


def rand_tense():
    pronoun = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]
    pronoun_imp = ["tu", "nous", "vous"]

    tense = [
        "présent",
        "impératif",
        "gérondif",
        "passe compose",
        "imparfait",
        "plus que parfait",
        "futur simple",
        "conditionnel",
        "conditionnel passé",
        "subjunctive",
    ]

    tense_choice = random.choice(tense)
    if tense_choice == "impératif":
        pronoun_choice = random.choice(pronoun_imp)
    else:
        pronoun_choice = random.choice(pronoun)

    return pronoun_choice, tense_choice


def read_and_remove_line(file_path):
    # Open the CSV file and read its contents
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        lines = list(reader)

    if not lines:
        print("The CSV file is empty.")
        return None

    # Read the first line
    line_to_read = lines[0]

    # Remove the first line from the list
    lines = lines[1:]

    # Write the remaining lines back to the CSV file
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lines)

    return line_to_read


def main():
    file_path = "verb bro/regular.csv"
    while True:
        line = read_and_remove_line(file_path)
        pronoun, tense = rand_tense()

        if line:
            print(f"Read line: {line}")
        else:
            print("No more lines to read.")
            break

        print(f"Pronoun: {pronoun}, Tense: {tense}")

        user_input = input("Enter a character (or 'q' to quit): ")
        if user_input == "q":
            print("Exiting the loop.")
            break
        else:
            print("----------------")


if __name__ == "__main__":
    main()
