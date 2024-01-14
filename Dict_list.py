import random

# Step 1: Create a list of random number of dictionaries
num_dicts = random.randint(2, 10)  # Generate a random number between 2 and 10
dict_list = []  # Empty list to store the dictionaries

for _ in range(num_dicts):
    random_dict = {}  # Create an empty dictionary
    num_keys = random.randint(1, 5)  # Generate a random number of keys for the dictionary

    for _ in range(num_keys):
        key = chr(random.randint(97, 122))  # Generate a random lowercase letter key
        value = random.randint(0, 100)  # Generate a random number value between 0 and 100
        random_dict[key] = value  # Add key-value pair to the dictionary

    dict_list.append(random_dict)  # Add the dictionary to the list

print("List of dictionaries:")
for i, dictionary in enumerate(dict_list, 1):
    print(f"Dictionary {i}: {dictionary}")
print()

# Step 2: Create a common dictionary based on the list of dictionaries
common_dict = {}  # Empty dictionary to store the common dictionary

for i, dictionary in enumerate(dict_list, 1):
    for key, value in dictionary.items():
        if key in common_dict:
            if value > common_dict[key]:
                common_dict[key] = value
                common_dict[f"{key}_{i}"] = common_dict.pop(key)
        else:
            common_dict[key] = value

print("Common dictionary:")
print(common_dict)
