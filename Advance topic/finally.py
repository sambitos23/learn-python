def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter a index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")  # it always use in function after return statement it will work

x = func1()
print(x)