l = [11, 2, 45, 6 , 3]
print(l) #[11, 2, 45, 6 , 3]

l.sort() #Sorting Method
print(l) #[2, 3, 6, 11, 45]
l.sort(reverse=True) #Reverse Sorting Method
print(l) #[45, 11, 6, 3, 2]

l.append("New") #Add Element at the End
print(l) #[2, 3, 6, 11, 45, 'New']

l.reverse() #To reverse a list
print(l) #['New', 2, 3, 6, 11, 45]

l = [11, 2, 45, 6 , 3]
print(l.index(6)) #Prints Index of 6 #3

print(l.count(45)) #1

l.insert(2, "HeHe") #(index, object)
print(l) #[11, 2, 'HeHe', 45, 6, 3]