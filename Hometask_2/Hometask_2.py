from random import randint, choice  # importing module
from string import ascii_lowercase  # importing module
final_dict, temp_dict = {},  {}  # create a dictionaries
dict_list = [{choice(ascii_lowercase): randint(0, 100)  # create the list dictionaries from 2 to 10
    for i in range(len(ascii_lowercase))}  # keys for dictionary are letters
    for j in range(randint(2, 10))]  # value for dictionary are random numbers from 0 to 100
#  Transform from list of dicts into dict of lists.
for dictionary in dict_list:
    for k, v in dictionary.items():
        temp_dict.setdefault(k, []).append(v)
#  Now choose only the biggest one
for k, v in temp_dict.items():
    if len(v) > 1:
        final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
    else: final_dict[k] = v[0]
print(dict_list)
print(temp_dict)
print(final_dict)
