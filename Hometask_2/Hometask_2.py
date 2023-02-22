import random
import string


# Create the list dictionaries from 2 to 10.
def create_dicts():
    output = []  # Dicts list
    for _ in range(random.randint(2, 10)):  # Dictionary counter
        dictionary = {}
        for _ in range(random.randint(1, 26)):  # Elements counter
            # Key(random letter), value(random number from 0 to 100)
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        output.append(dictionary)  # Append every dictionary to the list
    return output


output = {}

list_of_dicts = create_dicts()

c = 1
for cntr in list_of_dicts:
    for key, value in cntr.items():
        if key not in output:  # Check whether value exists previously
            output[key] = {str(c): value}
        else:
            output[key][str(c)] = value
    c += 1

my_dict = {}
for key, value in output.items():
    if len(output[key]) == 1:
        my_dict[key] = max(output[key].values())
    else:
        my_dict[key + "_" + str(max(output[key], key=output[key].get))] = max(output[key].values())


for i in range(len(list_of_dicts)):
    print(f'Dict {i+1}:  {list_of_dicts[i]}')  # Just for better displaying
print('')
print('dictionary with all value for key:', dict(output))
print('Final dictionary:', my_dict)
