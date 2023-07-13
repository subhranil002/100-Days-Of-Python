# Day 51 - seek() and tell() functions
In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.
## seek() function
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:
```python
with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
```
## tell() function
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:

```python
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)
```
## truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

Here is an example of how to use the truncate function:

```python
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())

```

# Day 52 - Lambda Functions in Python
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

```python
lambda arguments: expression
```
Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

Here is an example of how to use a lambda function:

```python
# Function to double the input
def double(x):
  return x * 2

# Lambda function to double the input
lambda x: x * 2
```
The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.

Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:

```python
# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
lambda x, y: x * y
```
Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

```python
# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')
```
In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later.

# Day 53 - Map, Filter and Reduce
In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

## map
The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

```python
map(function, iterable)
```
The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

Here is an example of how to use the map function:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))
```
In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list. The map function applies the lambda function to each element in the list and returns a new list containing the doubled numbers.

## filter
The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

```python
filter(predicate, iterable)
```
The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

Here is an example of how to use the filter function:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))
```
In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list and return only the even numbers. The filter function applies the lambda function to each element in the list and returns a new list containing only the even numbers.

## reduce
The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:
```python
reduce(function, iterable)
```
The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

Here is an example of how to use the reduce function:

```python
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)
```
In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 15.

It is important to note that the reduce function requires the functools module to be imported in order to use it.

# Day 54 - 'is' vs '==' in Python
In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

For example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```
In this case, a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.

One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:

```python
a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True
```
In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.

I hope this helps clarify the difference between is and == in Python!

# Day 55 - Exercise 5 : Stone Paper Scissor
Stone, Paper and Scissor is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a Stone, Paper, or a Scissor. The Paper beats the Stone, the Stone beats the Scissor, and the Scissor beats the Paper.
Write a python program to create a Stone Paper Scissor game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

# Day 56 - Introduction to Object-oriented programming
Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that are used to write program or code.
- 1). Procedural Programming
- 2). Object-Oriented Programming

The procedure we are following till now is the “Procedural Programming” approach. So, in this session, we will learn about Object Oriented Programming (OOP).
The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.

A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

An object is an instance of a class, and it contains its own data and methods. For example, you could create a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.

One of the key features of OOP in Python is encapsulation, which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This helps to protect the object's data and prevent it from being modified in unexpected ways.

Another key feature of OOP in Python is inheritance, which allows new classes to be created that inherit the properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.

Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.

In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.

# Day 57 - Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.
 

## Creating a Class:
Let us now create a class using the class keyword.
 
```python
class Details:
    name = "Rohan"
    age = 20
 ```

## Creating an Object:
Object is the instance of the class used to access the properties of the class
Now lets create an object of the class.

### Example:
```python
obj1 = Details() 
```

Now we can print values:

### Example:
```python
class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)
```
### Output:
```
Rohan
20
```

## self parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition. 

 

### Example:
```python
class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()
 
```
### Output:
```
My name is Rohan and I'm 20 years old.
```

# Day 58 - Constructors
A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class. 
The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
## Syntax of Python Constructor
```python
def __init__(self):
	# initializations
 ```
init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.

 ## Types of Constructors in Python
1. Parameterized Constructor
2. Default Constructor
  
### Parameterized Constructor in Python
When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members. 
#### Example:
``` python
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
```
#### Output:
```
Crab belongs to the Crustaceans group.
```
### Default Constructor in Python
When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
#### Example:
```python
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()
```
#### Output:
```
animal Crab belongs to Crustaceans group
```
# Day 59 - Python Decorators
Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
```python
@decorator_function
def my_function():
    pass
```

The @decorator_function notation is just a shorthand for the following code:
```python
def my_function():
    pass
my_function = decorator_function(my_function)
```
Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

## Practical use case
One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:
```python
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
```

In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.

## Conclusion
Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.

# Day 60 - Getters & Setters

## Getters
Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.
Here is an example of a simple class with a getter method:
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
```
In this example, the MyClass class has a single property, _value, which is initialized in the __init__ method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:
```python
>>> obj = MyClass(10)
>>> obj.value
10
```
## Setters
It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

Here is an example of a class with both getter and setter:

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
```
We can use setter method like this:
```python
>>> obj = MyClass(10)
>>> obj.value = 20
>>> obj.value
20
```
In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.

