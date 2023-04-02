info = {'name': 'Sambit', 'age': 22, 'eligible': True}
info2 = {'vote': 'yes', 'house': True, 'neighbour': 'yes', 211: 32}

info.update(info2)
info.clear()  # remove entire value of the dictionary

info2.pop('house')  # Remove specific key value pair
info2.popitem()  # Remove the last key value pair
print(info)
del info  # entirely delete the dictionary
del info2[211]  # delete specific
print(info2)
