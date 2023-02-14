from random import randint, choice  # importing module.
from string import ascii_lowercase  # importing module.


dictionary_all_values = {}
dictionary_max_values = {}
# Create the list dictionaries from 2 to 10.
list_with_dictionaries = [{choice(ascii_lowercase): randint(0, 100)
    for _ in range(len(ascii_lowercase))}  # create keys as lowercase letters.
    for _ in range(randint(2, 10))]  # create value with random numbers from 0 to 100.
#  Transform from list of dicts into dict of lists.
for dictionary in list_with_dictionaries:
    for key, value in dictionary.items():
        dictionary_all_values.setdefault(key, []).append(value)
#  Choose only the biggest one.
number_of_dict_with_maximum_value = 0
for key, value in dictionary_all_values.items():
    if len(value) >= 1:
        dictionary_max_values[key + "_" + str(value.index(max(value)) + 1)] = max(value)
    else:
        dictionary_max_values[key] = value[0]

print('list dictionaries: ', list_with_dictionaries)
print('dictionary with list of all values for key:', dictionary_all_values)
print('dictionary with max value:', dictionary_max_values)
