name = "Harry,Subhranil"
print(len(name),"\n") #15

#Positive Slicing -->
print("Positive Slicing -->")
print(name[0:5]) #Harry
print(name[6:15]) #Subhranil
print(name[:5],"\n") #Harry

#Negetive Slicing -->
#[0:-5] means [0:len(name)-5]
#Starts counting from the Right End
print("Negetive Slicing -->")
print(name[0:-5])
print(name[0:-8])
print(name[-10:-8])