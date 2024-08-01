# Iterating over a dictionary in Python allows you to access its keys and values or both together. Python offers several methods for iterating over dictionaries, including keys(), values(), items(), and direct iteration using a for loop.

# Here are some common ways to iterate over a dictionary:

# Iterating over keys:
# You can use the keys() method to iterate over the keys of the dictionary.

# python
# Copy code
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for key in my_dict.keys():
#     print(key)
# Iterating over values:
# You can use the values() method to iterate over the values of the dictionary.

# python
# Copy code
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for value in my_dict.values():
#     print(value)
# Iterating over items:
# You can use the items() method to iterate over key-value pairs (items) of the dictionary.

# python
# Copy code
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for key, value in my_dict.items():
#     print(key, value)
# Direct iteration:
# You can directly iterate over the dictionary, which implicitly iterates over its keys.

# python
# Copy code
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for key in my_dict:
#     print(key, my_dict[key])
# Each approach has its own use cases, and you can choose the one that best fits your needs based on whether you need to access keys, values, or both.
