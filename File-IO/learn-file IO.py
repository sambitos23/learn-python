# Read file
f = open('../f-string.py', 'r')
print(f)
text = f.read()
print(text)
f.close()

# Write file
f = open('myfile.txt', 'w')
f.write("Hello World")
f.close()
f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# Append file
f = open('myfile.txt', 'a')
f.write("\nHello World")
f.close()
f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# We don't have to use .close(), if we add with
with open('myfile.txt', 'a') as f:
    f.write("Hey, I am Sambit")
