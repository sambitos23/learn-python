marks = [12, 56, 32, 98, 12, 45, 1, 4]
index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Sambit, awasome\n\n")
        break
    index += 1


for index2, mark in enumerate(marks):
    print(mark)
    if index2 == 3:
        print("Sambit, awasome \n\n")
        break


for ind, mark in enumerate(marks, start=1):
    print(ind, mark)