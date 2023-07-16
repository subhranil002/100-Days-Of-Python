# Day 31 - Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

#### Example:
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 19, 5.9, 'Carla'}
 ```

Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

 **Quick Quiz:** Try to create an empty set. Check using the type() function whether the type of your variable is a set

## Accessing set items:
 

### Using a For loop
You can access items of set using a for loop. 

#### Example:
```python
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
  ```
#### Output:
```
False
Carla
19
5.9
```
# Day 32 - Set Methods
There are several in-built methods used for the manipulation of set.They are explained below
## isdisjoint():
The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```
#### Output:

False


## issuperset():
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
```
#### Output:

False\
False

## issubset():
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```
#### Output:

True
## add()
If you want to add a single item to the set use the add() method.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```
#### Output:

{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}
 
## update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```
#### Output:

{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}
 

 

## remove()/discard()
We can use remove() and discard() methods to remove items form list.

#### Example :
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
```
#### Output:

{'Delhi', 'Berlin', 'Madrid'}
 

 

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
```
#### Output:

KeyError: 'Seoul' 

## pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
```
#### Output:

{'Tokyo', 'Delhi', 'Berlin'}
Madrid
 

## del
del is not a method, rather it is a keyword which deletes the set entirely.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```
#### Output:

NameError: name 'cities' is not defined 
We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

 

What if we don’t want to delete the entire set, we just want to delete all items within that set?

 

## clear():
This method clears all items in the set and prints an empty set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```
#### Output:

set()
 

## Check if item exists
You can also check if an item exists in the set or not.

##### Example
```python
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
  ```
#### Output:

Carla is present.


## Joining Sets
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

 

## I. union() and update():
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
 ```

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)
```
#### Output:
```
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'} 
 
```
## II. intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
```
#### Output:
```
{'Madrid', 'Tokyo'}
 ```

#### Example :
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```
#### Output:
```
{'Tokyo', 'Madrid'}
```

## III. symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```
#### Output:
```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
 ```

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```
#### Output:
```
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
 ```

## IV. difference() and difference_update():
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
 ```

#### Example:
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```
#### Output:
```
{'Tokyo', 'Berlin', 'Madrid'}
```

# Day 33 - Python Dictionaries
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

 

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
```
## Accessing Dictionary items:
 

### I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
```
#### Output:
```
Karan
True
 ```

### II. Accessing multiple values:
We can print all the values in the dictionary using values() method.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
```
#### Output:
```
dict_values(['Karan', 19, True])
 ```

### III. Accessing keys:
We can print all the keys in the dictionary using keys() method.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
```
#### Output:
```
dict_keys(['name', 'age', 'eligible'])
 ```

### IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
```
#### Output:
```
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```

# Day 34 - Dictionary Methods
Dictionary uses several built-in methods for manipulation.They are listed below
## update() 
The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
 ```

 

## Removing items from dictionary:
There are a few methods that we can use to remove items from dictionary.

 

### clear():
The clear() method removes all the items from the list. 
#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
```
#### Output:
```
{}
 ```

#### pop():
The pop() method removes the key-value pair whose key is passed as a parameter.
#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19}
 ```

### popitem(): 
The popitem() method removes the last key-value pair from the dictionary.
#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
 ```

### del:
we can also use the del keyword to remove a dictionary item. 

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
```
#### Output:
```
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
 ```

If key is not provided, then the del keyword will delete the dictionary entirely.

#### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
```
#### Output:
```
NameError: name 'info' is not defined
```

# Day 35 - Python - else in Loop
As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
## Syntax
```
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```
## Example:
```
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
```
## Output:
```
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

# Day 36 - Exception Handling
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
## Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

## Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed. 

 ### Syntax:
 ```python
 try:
      #statements which could generate 
      #exception
except:
      #Soloution of generated exception
```
### Example:
```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
 ```

### Output:
```
Enter an integer: 6.022
Number entered is not an integer.
```

# Day 37 - Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.
## Syntax:
```
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
    
   
```
The finally block is executed irrespective of the outcome of try……except…..else blocks\
One of the important use cases of finally block is in a function which returns a value.
## Example:
```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
 ```

### Output 1:
```
Enter an integer: 19
Integer Accepted.
This block is always executed.
```
### Output 2:
```
Enter an integer: 3.142
Number entered is not an integer.
This block is always executed.
```

# Day 38 - Raising Custom errors 
In python, we can raise custom errors by using the `raise`  keyword. 
```python
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
```

In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

## Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
```python
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

# Day 39 - Exercise 3: Solution

[1024. Kaun Banega Crorepati.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1024.%20Kaun%20Banega%20Crorepati.py)

# Day 40 - Exercise 4 : Create a Secret Code Language

Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
