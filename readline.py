f = open("marks.txt", "r")
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]  # type -> string
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in bengali is: {m2}")
    print(f"marks of student {i} in english is: {m3}")
