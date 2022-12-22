import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

Hour = int(time.strftime("%H"))

if (Hour<12 and Hour>=5):
    print("Good Morning")
elif(Hour<16 and Hour>=12):
    print("Good Noon")
elif(Hour<18 and Hour>=16):
    print("Good Afternoon")
elif(Hour<20 and Hour>=18):
    print("Good Evening")
else:
    print("Good Night")