marks = [12, 56, 32, 98, 12, 45, 1, 4]

index = 0
for mark in marks: # Old Technique
    print(mark)
    if(index == 3):
        print("Awesome")
    index += 1

# Output -->
# 12
# 56      
# 32      
# 98      
# Awesome 
# 12      
# 45      
# 1       
# 4     

for index, mark in enumerate(marks): # Introducing Enumerate
    print(mark)
    if(index == 3):
        print("Awesome")
        
# Output -->
# 12
# 56      
# 32      
# 98      
# Awesome 
# 12      
# 45      
# 1       
# 4     
        
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output -->
# 0 apple 
# 1 banana
# 2 mango
    
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

# Output -->
# 0 red   
# 1 green 
# 2 blue
    
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
    
# Output -->
# 0 h     
# 1 e     
# 2 l     
# 3 l     
# 4 o