l: list[int] = [11, 45, 1, 2, 4, 6]
print(l)
print(l.index(1))  # it returns first occurrence in the list item in which index 1 is present.
l.append(7)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

li = [11, 1, 45, 1, 2, 4, 6, 1]
print(li.count(1))

li.insert(1, 899)
print(li)

li.reverse()
print(li)

m = li.copy()
m[0] = 0
print(m)

x = [900, 878, 77]
k = l + x  # concatenate 2 list
print(k)
li.extend(x)
print(li)
