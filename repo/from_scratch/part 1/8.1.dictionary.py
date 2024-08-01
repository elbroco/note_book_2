"""
my_dict = {
    'name' : 'ivaen',
    'age' : 43,
    'job' : 'dj'
}

print(my_dict)

print(my_dict['age'])
print(my_dict.get('job'))

print('name' in my_dict)
print('name1' in my_dict)
print(43 in my_dict)


"""

DATA2=  {
    "name": "Harry Potter",
    "species": "human",
    "gender": "male",
    "house": "Gryffindor",
    "dateOfBirth": "31-07-1980",
    "yearOfBirth": 1980,
    "ancestry": "half-blood",
    "eyeColour": "green",
    "hairColour": "black",
    "programas" : ['hechiceria 1', 'posiones 2'],
    "wand": {
      "wood": "holly",
      "core": "phoenix feather",
      "length": 11
    } 
}

DATA2['name'] = 'maradona'
DATA2['programas'].append('futbol 1')
del DATA2['species']

print(DATA2)