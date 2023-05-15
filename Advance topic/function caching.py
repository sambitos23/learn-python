from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(2))
print("done for 2")
print(fx(20))
print("done for 20")
print(fx(40))
print("done for 40")

print(fx(2))
print("done for 2")
print(fx(20))
print("done for 20")
print(fx(40))
print("done for 40")
print(fx(12))
print("done for 12")
