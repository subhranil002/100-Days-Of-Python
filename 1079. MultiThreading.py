import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    time1 = time.perf_counter()

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)


main()

# Sleeping for 4 seconds
# Sleeping for 2 seconds
# Sleeping for 1 seconds
# 4.001476800011005


def poolingDemo():
    time1 = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

    time2 = time.perf_counter()
    print(time2 - time1)


poolingDemo()

# Sleeping for 3 seconds
# Sleeping for 5 seconds
# Sleeping for 1 seconds
# Sleeping for 2 seconds
# 3
# 5
# 1
# 2
# 5.002162599994335
