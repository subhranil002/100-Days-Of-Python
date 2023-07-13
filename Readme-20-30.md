# Day 21 - Function Arguments and return statement
There are four types of arguments that we can provide in a function:

- Default Arguments
- Keyword Arguments
- Variable length Arguments
- Required Arguments
### Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:
```python
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```
Output:
```
Hello, Amy Jhon Whatson
 ```

### Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:
```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```
Output:
```
Hello, Jade Peter Wesker
 ```

### Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example 1: when number of arguments passed does not match to the actual function definition.
```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
```
Output:
```
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
 ```

Example 2: when number of arguments passed matches to the actual function definition.
```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
```
Output:
```
Hello, Peter Ego Quill
 ```

### Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

#### Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:
```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```
Output:
```
Hello, James Buchanan Barnes
 ```

#### Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:
```python
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
```
Output:
```
Hello, James Buchanan Barnes
```

## return Statement
The return statement is used to return the value of the expression back to the calling function.

 

Example:
```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
 ```

Output:
```
Hello, James Buchanan Barnes
```

# Day 22 - Python Lists
- Lists are ordered collection of data items.
 - They store multiple items in a single variable.
 - List items are separated by commas and enclosed within square brackets [].
 - Lists are changeable meaning we can alter them after creation.

Example 1:
```python
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```
Output:
```
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```

Example 2:
```python
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```
Output:
```
['Abhijeet', 18, 'FYBScIT', 9.8]
```
As we can see, a single list can contain items of different data types.

# Day 23 - List Methods
## list.sort()
This method sorts the list in ascending order. The original list is updated
### Example 1:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```
### Output:
```
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
 
```
What if you want to print the list in descending order?\
We must give reverse=True as a parameter in the sort method.

### Example:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```
#### Output:
```
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
 ```

The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

 

## reverse()
This method reverses the order of the list. 

#### Example:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```
#### Output:
```
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
 ```

## index()
This method returns the index of the first occurrence of the list item.
#### Example:
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
Output:
```
1
3
 ```

## count()
Returns the count of the number of items with the given value.
#### Example:
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
```
#### Output:
```
2
3
 ```

## copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list. 

#### Example:
```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']
```
## append():
This method appends items to the end of the existing list.

#### Example:
```python
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green']
 ```
## insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

#### Example:
```python
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
 ```
## extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#### Example 1:
```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
 ```
## Concatenating two lists:
You can simply concatenate two lists to join two lists.

#### Example:
```python
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

# Day 24 - Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

 

### Example 1:
```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```
### Output:
```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```

### Example 2:
```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```
### Output:
```
('Abhijeet', 18, 'FYBScIT', 9.8)
```

# Day 25 - Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

#### Example:
```python
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
```
#### Output:
```
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
 ```

Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

 

However, we can directly concatenate two tuples without converting them to list.

#### Example:
```python
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
```
#### Output:
```
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
```

# Day 26 - Excersice 2: Solution

[1013. Good Morning Sir.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1013.%20Good%20Morning%20Sir.py)

# Day 27 - Excersice 3

## Create a program capable of displaying questions to the user like KBC. 
Use List data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.

# Day 28 - String formatting in python
String formatting can be done in python using the format method.
```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```
## f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

### Example
```python
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  
```
### Output:
```
Hello, My name is Tushar and I'm 23 years old.
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.
### Example
```python
print(f"{2 * 30})"  
```
### Output:
```
60
```

# Day 29 - Docstrings in python
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. 
## Example
```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

```
Here, 

'''Takes in a number n, returns the square of n''' 
is a docstring which will not appear in output

## Output:
```
25
```
Here is another example:
```python
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
```
## Python Comments vs Docstrings
### Python Comments

Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.
### Python docstrings

As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

We can access these docstrings using the __doc__ attribute.
## Python __doc__ attribute
Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their __doc__ attribute. We can later use this attribute to retrieve this docstring.

## Example
```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```
## Output:
Takes in a number n, returns the square of n

# Day 30 - Recursion in python
Recursion is the process of defining something in terms of itself.

## Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
## Example:
```python
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))
 ```

## Output:
```
number:  7
Factorial:  5040
```
