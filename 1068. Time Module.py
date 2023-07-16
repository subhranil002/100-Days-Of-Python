import time


print(4)
time.sleep(3)
print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
