# MAP
# def cube(x):
#     return x*x*x

l = [1, 2, 4, 6, 8, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))

# newl = list(map(cube, l))
newl = list(map(lambda x: x * x * x, l))
print("map", newl)

# FILTER

# def fliter_function(a):
#     return a > 4

new_newl = filter(lambda x: x > 4, l)
print("filter", list(new_newl))

# REDUCE
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print("reduce", sum)
