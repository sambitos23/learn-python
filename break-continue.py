for i in range(12):
    print("5 X", i, "=", 5 * i)
    if i == 10:
        break
print("Loop closed")

for i in range(13):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)
