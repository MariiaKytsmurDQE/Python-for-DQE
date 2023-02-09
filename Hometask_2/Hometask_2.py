from random import randint, choice
from random import randint, choice
from string import ascii_lowercase
final_dict, tmp_dict = {},  {}
rand_list = [{choice(ascii_lowercase): randint(0, 100)
for i in range(len(ascii_lowercase))}
for j in range(randint(2, 10))]
#Transform from list of dicts into dict of lists.
for dictionary in rand_list:
  for k, v in dictionary.items():
    tmp_dict.setdefault(k, []).append(v)
#Now choose only the biggest one
for k, v in tmp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]
print(rand_list)
print(tmp_dict)
print(final_dict)
