from collections import defaultdict
import random
import string


# Create the list dictionaries from 2 to 10.
def create_dicts():
    output = []  # Dicts list
    for dict_number in range(random.randint(2, 10)):  # Dictionary counter
        dictionary = {}
        for elem_number in range(random.randint(1, 26)):  # Elements counter
            # Key(random letter), value(random number from 0 to 100)
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        output.append(dictionary)  # Append every dictionary to the list
    return output


output = defaultdict(lambda: float('-inf'))

list_of_dicts = create_dicts()


for cntr in range(0, len(list_of_dicts)):  # Create a counter for later adding of '_number_of_dictionary' for the same keys
    for key, value in list_of_dicts[cntr].items():
        if output[key] != float('-inf'):  # Check whether value exists previously
            if output[key] > value:  # If stored value > actual than we do nothing
                continue
            del output[key]  # Delete key with max value
            key = f'{key}_{cntr + 1}'  # Create new key with adding '_number_of_dictionary'

        output[key] = max(output[key], value)  # Add key: value


for i in range(0, len(list_of_dicts)):
    print(f'Dict {i+1}:  {list_of_dicts[i]}')  # Just for better displaying
print('')
print('dictionary with max value:', dict(output))



