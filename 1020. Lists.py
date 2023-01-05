l = [3, 5, 6, "Subhranil", True] #Initiating a List
print(l) #[3, 5, 6, "Subhranil", True]
print(type(l)) #<class 'list'>
print(l[3]) #Subhranil

#Calculate Nagative Index -->
print(l[-3]) #6
print(l[len(l)-3]) #6
print(l[5-3]) #6
print(l[2]) #6

if 3 in l:
    print("Yes") #Yes
    
if "nil" in "Subhranil":
    print("Yes") #Yes
    
print(l) #[3, 5, 6, 'Subhranil', True]
print(l[1:-1]) #[5, 6, 'Subhranil']  
print(l[1:4:2]) #[5, 'Subhranil']

ll = [i for i in range(4)]
print(ll) #[0, 1, 2, 3]

ll = [i for i in range(4)]
print(ll) #[0, 1, 2, 3]

ll = [i*i for i in range(10) if i%2==0]
print(ll) #[0, 4, 16, 36, 64]  