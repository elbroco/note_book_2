def find_max_min_except_last(lst):
    if len(lst) < 2:
        return None, None, None

    numbers_except_last = lst[:-1]
    max_value = max(numbers_except_last)
    min_value = min(numbers_except_last)
    last_item = lst[-1]

    return max_value, min_value, last_item

data = input("Coloca los datos: ")
dict1 = data.split()

data1 = input("Coloca los datos: ")
dict2 = data1.split()

data2 = input("Coloca los datos: ")
dict3 = data2.split()

f_dict = [dict1, dict2, dict3]

sorted_f_dict = sorted(f_dict)

for lst in sorted_f_dict:
    max_val, min_val, last_item = find_max_min_except_last(lst)
    if max_val is not None and min_val is not None:
        print(f"For list {lst}:")
        print(f"Maximum value (excluding the last): {max_val}")
        print(f"Minimum value (excluding the last): {min_val}")
        print(f"Last item in the list: {last_item}")
        print()
    else:
        print("The list is empty or has only one element.")

