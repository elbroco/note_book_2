import utils

keys, values = utils.get_population()
print(keys, values)

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

country = input('Type Country => ')

result = utils.population_by_country(data, country)
print(result)


# Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta.


# if __name__ == "__main__":
# 	run()