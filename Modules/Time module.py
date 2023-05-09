import time


def UsingWhile():
    i = 0
    while i<5000:
        i = i+1
        print(i)


def UsingFor():
    for i in range(5000):
        print(i)


init = time.time()
UsingWhile()
while_loop = time.time() - init
init = time.time()
UsingFor()
print("For loop", time.time() - init)
print("While loop", while_loop)



print(4)
time.sleep(3)
print("This is printed after 3 seconds")


t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)