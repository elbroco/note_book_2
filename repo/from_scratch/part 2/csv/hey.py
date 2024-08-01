import csv

def xd(path):
    values = []

    with open(path) as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            values.append(row[1])
    
    total = sum(list(map(lambda x: int(x), values)))
    return total

    


print(xd('from_scratch/part 2/csv/data2.csv'))