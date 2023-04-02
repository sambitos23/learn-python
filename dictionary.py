info = {'name': 'Sambit', 'age': 22, 'eligible': True}

print(info)
print(info.keys())
print(info.values())

print(info['name'])
print(info.get('name2'))

print(info.items())

for key, value in info.items():
    print(f"The value cooresponding to the key {key} is {value}")