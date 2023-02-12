from random import randint, choice  # importing module
from string import ascii_lowercase  # importing module
final_dict, temp_dict = {},  {}  # create a dictionaries
dict_list = [{choice(ascii_lowercase): randint(0, 100)  # create the list dictionaries from 2 to 10
    for _ in range(len(ascii_lowercase))}  # keys for dictionary are letters
    for _ in range(randint(2, 10))]  # value for dictionary are random numbers from 0 to 100
#  Transform from list of dicts into dict of lists.
for dictionary in dict_list:
    for key, value in dictionary.items():
        temp_dict.setdefault(key, []).append(value)
#  Now choose only the biggest one
number_of_dict_with_maximum_value = 0
for key, value in temp_dict.items():
    if len(value) > 1:
        final_dict[key + "_" + str(value.index(max(value)) + 1)] = max(value)
    else:
        final_dict[key] = value[0]
print('list dictionaries: ', dict_list)
print('dictionary with list of all values for key:',temp_dict)
print('dictionary with max value:', final_dict)