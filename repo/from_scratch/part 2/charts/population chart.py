import random
import csv
import matplotlib.pyplot as plt

def info(path):
    random_number = random.randint(0, 234)
    print("Random number:", random_number)

    with open(path) as archivo:
        reader = csv.reader(archivo)
        header = next(reader)  # Read the headers from the first row
        # Filter the headers to get the ones in the range [5, 12]
        headers = [header[i] for i in range(5, 12)]

        for i, row in enumerate(reader):
            if i == random_number:
                population = []
                for j in range(3, 12):  # Assuming columns 3 to 11 contain population data
                    try:
                        population.append(int(row[j]))
                    except ValueError:
                        # Handle non-integer values gracefully (e.g., skip them)
                        pass

                headers.reverse()
                population.reverse()

                print(headers)
                print(population)
                generate_bar_chart(headers, population)
                
                break  # Stop the loop after finding the random row

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()  # Create figure and axis
    ax.bar(labels, values)  # Create bar chart
    plt.show()

path = 'C:\\Users\\Alexandra la Mejor\\Desktop\\python1\\from_scratch\\part 2\\charts\\data.csv'

info(path)