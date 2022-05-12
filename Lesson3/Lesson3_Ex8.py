data_dict = {}
data_dict['name'] = input("Your name (single only):\n")
data_dict['age'] = input("Your age (single only):\n")
films = input("Your favorite films (use comma)::\n")
data_dict['films'] = list(films.split(','))
print(data_dict)
print(list(data_dict.keys()))
replace_key = input("What element to replace?\n")
replace_value = input("Which value to replace?\n")
if replace_key == 'films':
    replace_value = list(replace_value.split(','))
data_dict.update({replace_key: replace_value})
print(data_dict)
new_key = input("Enter any key for dictionary (single only):\n")
if new_key not in data_dict:
    new_value = input("Enter any value for new key (single only):\n")
    print(new_value)
else:
    print(data_dict[new_key])
