def my_generator():
    for i in range(5):
        yield i   # it will execute on the fly


gen = my_generator()
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)

