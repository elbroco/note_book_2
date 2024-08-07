import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data # esto lo transforma en dict

if __name__ == '__main__':
  data = read_csv('from_scratch/part 2/csv/data.csv')
  print(data[0]) # ahi puedo elegir a que fila acceder