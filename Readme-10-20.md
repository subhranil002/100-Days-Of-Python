# Day 11 - What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters. 
## Example
```python
name = "Harry"
print("Hello, " + name)
```
## Output
Hello, Harry

Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same. 

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: 
```He said, "I want to eat an apple".```
We will definitely use single quotes for our convenience
```python
print('He said, "I want to eat an apple".')
```

## Multiline Strings
If our string has multiple lines, we can create them like this: 
```python 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

## Accessing Characters of a String
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.\
Square brackets can be used to access elements of the string.

```python 
print(name[0])
print(name[1])

```

## Looping through the string
We can loop through strings using a for loop like this: 
```python
for character in name:
    print(character)
```

Above code prints all the characters in the string name one by one!

# Day 12 - String Slicing & Operations on String
# Length of a String
We can find the length of a string using len() function.

## Example:
```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```
## Output:
Mango is a 5 letter word.
# String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array. 

## Example:
```python
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
```
## Output:
```
Apple
i
```
 

Note: This method of specifying the start and end index to specify a part of a string is called slicing. 
## Slicing Example:
```python
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
```
## Output:
```
Apple
Pie
pleP
ApplePie
```
# Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.
## Example:
```python
alphabets = "ABCDE"
for i in alphabets:
    print(i)
  ```
## Output:
```
A
B
C
D
E
```

# Day 13 - String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.


## upper() :
The upper() method converts a string to upper case.

### Example:
```python
str1 = "AbcDEfghIJ"
print(str1.upper())
```
### Output:
```
ABCDEFGHIJ
 ```

## lower()
The lower() method converts a string to lower case.
### Example:
```python
str1 = "AbcDEfghIJ"
print(str1.lower())
```
### Output:
```
abcdefghij
 ```

## strip() :
The strip() method removes any white spaces before and after the string.
### Example:
```python
str2 = " Silver Spoon "
print(str2.strip)
```
### Output:
```
Silver Spoon
``` 

## rstrip() : 
the rstrip() removes any trailing characters.
Example:
```python
str3 = "Hello !!!"
print(str3.rstrip("!"))
```
### Output:
```
Hello
 ```

## replace() : 
The replace() method replaces all occurences of a string with another string.
Example:
```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```
### Output:
```
Silver Moon
 ```

## split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.
### Example:
```python
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```
### Output:
```
['Silver', 'Spoon']
There are various other string methods that we can use to modify our strings.
```
 

## capitalize() : 
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
### Example:
```python
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```
### Output:
```
Hello
Hello world
```

## center() : 
The center() method aligns the string to the center as per the parameters given by the user.
### Example:
```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```
### Output:
```
            Welcome to the Console!!!
 ```

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

### Example:
```python
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```
### Output:
```
............Welcome to the Console!!!.............
 ```

## count() :
The count() method returns the number of times the given value has occurred within the given string.
### Example:
```python
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```
### Output:
```
4
```
 

## endswith() : 
The endswith() method checks if the string ends with a given value. If yes then return True, else return False. 
### Example :
```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```
### Output:
```
True
```
We can even also check for a value in-between the string by providing start and end index positions.

### Example:
```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```
### Output:
```
True
 ```

## find() : 
The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
### Example:
```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```
### Output:
```
10
 ```

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:
```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```
### Output:
```
-1
 ```

## index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
### Example:
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```
### Output:
```
13
 ```

As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```
### Output:
```
ValueError: substring not found
 ```

## isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
### Example 1:
```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```
Output:
```
True
 ```
## isalpha() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
### Example :
```python
str1 = "Welcome"
print(str1.isalpha())
```
### Output:
```
True
 ```

## islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False. 
### Example:
```python
str1 = "hello world"
print(str1.islower())
```
### Output:
```
True
 ```

## isprintable() :
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
### Example :
```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```
### Output:
```
True
 ```
## isspace() :
The isspace() method returns True only and only if the string contains white spaces, else returns False.
### Example:
```python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```
### Output:
```
True
True
 ```

## istitle() : 
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
### Example:
```python
str1 = "World Health Organization" 
print(str1.istitle())
```
### Output:
```
True
 ```

### Example:
```python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```
### Output:
```
False
 ```

## isupper() :
The isupper() method returns True if all the characters in the string are upper case, else it returns False. 
### Example :
```python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
```
### Output:
```
True
 ```
  

## startswith() :
The endswith() method checks if the string starts with a given value. If yes then return True, else return False. 
### Example :
```python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
```
### Output:
```
True
 ```

## swapcase() : 
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
### Example:
```python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
```
### Output:
```
pYTHON IS A iNTERPRETED lANGUAGE
 ```

### title() :
The title() method capitalizes each letter of the word within the string.
### Example:
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```
### Output:
```
He'S Name Is Dan. Dan Is An Honest Man.
```

# Day 14 - if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:
- if
- if-else
- if-else-elif
- nested if-else-elif.
## An if……else statement evaluates like this:

### if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\
### if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.
 ## Example:
```python
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```
## Output:
```
Alexa, do not add Apples to the cart.
```

# elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
### Working of an elif statement
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.\
.\
.\
.\
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

## Example:
```python
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
```
## Output:
```
Number is Zero.
```

# Nested if statements
We can use if, if-else, elif statements inside other if statements as well. \
Example:
```python
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```
Output:
```
Number is between 11-20
```

# Day 15 - Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
```python
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
```

# Day 16 - Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.
## Syntax:
```python
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
```
### Example:
```python
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
```
### Output:
```
x % 2 == 0 and case is 4
```

# Day 17 - Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 
# The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

## Example: iterating over a string:

```python 
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```
## Output:

A, b, h, i, s, h, e, k,
 

## Example: iterating over a list:

``` python 
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```
## Output:

Red\
Green\
Blue\
Yellow

Similarly, we can use loops for lists, sets and dictionaries.
## range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

## Example:
```python
for k in range(5):
    print(k)
```
## Output:

0\
1\
2\
3\
4\
Here, we can see that the loop starts from 0 by default and increments at each iteration.

 

But we can also loop over a specific range.

## Example:
```python
for k in range(4,9):
    print(k)
```
## Output:

4\
5\
6\
7\
8

# Day 18 - Python while Loop
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop. 
## Example:

```python 
count = 5
while (count > 0):
  print(count)
  count = count - 1
```
## Output:
```
5
4
3
2
1
```

Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

# Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed. 

## Example:

```python 
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```
## Output:
```
5
4
3
2
1
counter is 0
```

# Day 19 - break statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
## example

```python '
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```
### output
```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Mississippi
```

## Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
## example
```python
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
  ```
  ## output
  ```
2
4
6
8
0

```

# Day 20 - Python Functions
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

 

There are two types of functions:

1. Built-in functions
2. User-defined functions
 

 ## Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

 

## User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

### Syntax:
```python
def function_name(parameters):
  pass
  # Code and Statements
```
 
- Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
 - Any parameters and arguments should be placed within the parentheses.
 - Rules to naming function are similar to that of naming variables.
 - Any statements and other code within the function should be indented.
### Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:
```python
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```
Output:
```
Hello, Sam Wilson
```

