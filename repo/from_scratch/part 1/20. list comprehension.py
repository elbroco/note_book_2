#element for element in iterable

numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)



'''
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)

'''

#for
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]

#List Comprehension


days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

newlist = [i for i in days if "a" in i]

print(newlist) # ["martes", "sabado"]