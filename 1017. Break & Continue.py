#Break Statement -->
print(("Break Statement -->"))
for i in range(1,13):
    print(i,end=" ") #1 2 3 4 5 6 7 8 9 10 11 12
print("\nExecuted Nomarlly")
for i in range(1,13):
    if (i==11):
        break
    print(i,end=" ",) #1 2 3 4 5 6 7 8 9 10
print("\nExecuted With Break Statement\n")

#Continue Statement -->
print(("Continue Statement -->"))
for i in range(1,13):
    print(i,end=" ") #1 2 3 4 5 6 7 8 9 10 11 12
print("\nExecuted Nomarlly")
for i in range(1,13):
    if (i==11):
        print("\nThis will print instred of 11")
        continue
    print(i,end=" ") #1 2 3 4 5 6 7 8 9 10
                     #This will print instred of 11
                     #12
print("\nExecuted With Break Statement")