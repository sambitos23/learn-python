with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)
    print(f.tell())

    # Read the nex 5 bytes
    data = f.read(5)
    print(data)
