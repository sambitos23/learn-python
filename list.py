marks = [3, 5, 7, "string", True]
print(marks)
print(type(marks))
print(marks[0])

print("negative index")
print(marks[-3])
print(marks[len(marks) - 3])

if 7 in marks:
    print("Yes")
else:
    print("No")

print(marks)
print(marks[:])
print(marks[0:len(marks)])  # default value in :
print(marks[1:-1])
print(marks[1:4:2])  # jump to index is 2

# list comprehension
lst = [i for i in range(4)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
