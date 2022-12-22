age = 18

print(age>18) #False
print(age<18) #False
print(age==18) #True
print(age!=18) #False

newAge = int(input("Enter age to Drive :")) #19
if(newAge>18):
    print("You can Drive") #This statement will print
    if(newAge>45):
        print("Just go to drive")
    else:
        print("Please Drive Slow :)") #This statement will print
elif(newAge==18): #elif = (else if)
    print("You can Drive")
else:
    print("You can not Drive")