import random
import csv
import matplotlib.pyplot as plt



def extract_country_names(path):
    country_names = []  # Initialize an empty list to store country names

    with open(path) as archivo:
        reader = csv.reader(archivo)

        # Skip the first row (header)
        next(reader)

        for row in reader:
            # Assuming the country name is in the first column (index 0) of each row
            country_names.append(row[2])

    return country_names

def extract_population_percentage(path):
    percentages = []  # List to store country names

    with open(path) as archivo:
        reader = csv.reader(archivo)

        # Skip the first row (header)
        next(reader)

        for row in reader:
            # Append the last element of the row to the countries list
            percentages.append(float(row[-1]))

    return percentages


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

path = 'C:\\Users\\Alexandra la Mejor\\Desktop\\python1\\from_scratch\\part 2\\charts\\data.csv'




country_names = extract_country_names(path)
population_p = extract_population_percentage(path)


generate_pie_chart(country_names, population_p)
