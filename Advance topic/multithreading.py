import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


def main():
    # time1 = time.perf_counter()
    # # Normal Code
    # func(4)
    # func(3)
    # func(2)
    # time2 = time.perf_counter()
    # print(time2-time1)

    time1 = time.perf_counter()
    # Same code using thread
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[3])
    t3 = threading.Thread(target=func, args=[2])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # Calculating time
    time2 = time.perf_counter()
    print(time2 - time1)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 2)
        # future2 = executor.submit(func, 3)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()
