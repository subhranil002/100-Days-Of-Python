def average(*numbers):
    print(type(numbers)) #<class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum +i
    # print("Average is =",sum/len(numbers)) #Average is = 5.5
    return sum/len(numbers)
    
avg = average(4,5,6,7)
print(avg) #Average is = 5.5

def name(**name):
    print(type(name)) #<class 'dict'>
    print("Wellcome to,",name["fname"],name["mname"],name["lname"]) #Wellcome to, World Wide Web
    
name(mname = "Wide",lname="Web",fname="World")