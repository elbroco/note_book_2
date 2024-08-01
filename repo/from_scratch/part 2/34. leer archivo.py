# Define the correct path
path = "C:\\Users\\Alexandra la Mejor\\Desktop\\python1\\from_scratch\\part 2\\texto.txt"

file = open(path)
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file:
  print(line)

file.close()

with open(path) as file:
  for line in file:
    print(line)
