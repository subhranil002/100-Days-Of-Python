#Simple Strings -->
print("Simple Strings -->")
Name = "Subhranl"
Friend = "None"
print("Hello",Name,"\n") #Hello Subhranl

#Multilevel Strings -->
print("Multilevel Strings -->")
apple = 'He said, "I want to eat a apple"'
#OR
apple = "He said, 'I want to eat a apple'"
print(apple,"\n") #He said, 'I want to eat a apple'

#Multiple Line Strings -->
print("Multiple Line Strings -->")
String = '''Hello !
Hi!
How 'Are' You ?
"Okay"
Bye!'''
print(String,"\n") #Hello!
                   #Hi!
                   #How 'Are' You ?
                   #"Okay"
                   #Bye !
              
#Character index of a Word -->
print("Character index of a Word -->")
Name = "Subhranl"
print(Name) #Subhranl
print(Name[0]) #S
print(Name[1]) #u
print(Name[7],"\n") #l

#Character index of a String -->
print("Character index of a String -->")
String = "Let's Use A String"
print(String) #Let's Use A String
print(String[0]) #L
print(String[3]) #'
print(String[5]) #Will print a Space
print(String[6],"\n") #U

#Printing All Characters Of A String -->
print("Printing All Characters Of A String -->")
String = "Let's Use A For Loop"
for char in String:
    print(char) #Prints Every Characters Once
