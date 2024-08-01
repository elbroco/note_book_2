print('Hola')

def my_print(text):
  print(text * 2)

my_print('Este es my texto')
my_print('Hola')

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b)

suma(1 ,5) # 6
suma(10, 4) # 14


# -------------
#return 

def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)