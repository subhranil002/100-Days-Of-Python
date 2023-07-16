# Day 81 - Hybrid Inheritance & Hierarchical Inheritance in Python

## Hybrid Inheritance
Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

### Syntax
The syntax for implementing Hybrid Inheritance in Python is the same as for implementing Single Inheritance, Multiple Inheritance, or Hierarchical Inheritance.


Here's the syntax for defining a hybrid inheritance class hierarchy:
```python 
class BaseClass1:
  # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods

```
### Example
Consider the example of a `Student` class that inherits from the `Person` class, which in turn inherits from the `Human` class. The `Student` class also has a `Program` class that it is associated with.

```python
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()
```
In this example, the `Student` class inherits from the `Person` class, which in turn inherits from the `Human` class. The `Student` class also has an association with the `Program` class. This is an example of `Hybrid Inheritance` in action, as it uses both Single Inheritance and Association to achieve the desired inheritance structure.

To create a `Student` object, we can do the following:
```python
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()
```
### Output
```python
Name: John Doe
Age: 25
Address: 123 Main St.
Program Name: Computer Science
Duration: 4
```
As we can see from the output, the `Student` object has access to all the attributes and methods of the `Person` and `Human` classes, as well as the `Program` class through association. 

In this way, hybrid inheritance allows for a flexible and powerful way to inherit attributes and behaviors from multiple classes in a hierarchy or chain.

## Hierarchical Inheritance

Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.

Here's an example to illustrate the concept of hierarchical inheritance in Python:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)
```
In the above code, the `Animal` class acts as the base class for two subclasses, `Dog` and `Cat`. The `Dog` class and the `Cat` class inherit the attributes and methods of the `Animal` class. However, they can also add their own unique attributes and methods.

Here's an example of creating objects of the `Dog` and `Cat` classes and accessing their attributes and methods:

```python
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
```
### Output:
```
Name: Max
Species: Dog
Breed: Golden Retriever
Name: Luna
Species: Cat
Color: Black
```
As we can see from the outputs, the `Dog` and `Cat` classes have inherited the attributes and methods of the `Animal` class, and have also added their own unique attributes and methods.

In conclusion, hierarchical inheritance is a way of establishing relationships between classes in a hierarchical manner. It allows multiple subclasses to inherit from a single base class, which helps in code reuse and organization of code in a more structured manner.

# Day 82 - Exercise 8: Solution

[1061. Merge the PDF.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1061.%20Merge%20the%20PDF.py)

# Day 83 - Exercise 9: ShoutOuts To Everyone

Write a program to pronounce list of names using pyttsx3. 
If you are given a list l as follows:
```python
l = ["Rahul", "Nishant", "Harry"]
```
Your program should pronouce:
```
Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry
```
Note: If you are not using windows, try to figure out how to do the same thing using some other package

# Day 84 - The time Module in Python
The `time` module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the `time` module in Python and see how it can be used in different scenarios.

## time.time()
The `time.time()` function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time. Here's an example:
```python
import time
print(time.time())
# Output: 1602299933.233374
```
As you can see, the function returns the current time as a floating-point number, which can be used for various purposes, such as measuring the duration of an operation or the elapsed time since a certain point in time.

## time.sleep()
The `time.sleep()` function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. Here's an example:
```python
import time

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376
```
As you can see, the function `time.sleep()` suspends the execution of the program for 2 seconds, allowing other parts of the program to run during that time.

## time.strftime()
The `time.strftime()` function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. Here's an example:
```python
import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33
```
As you can see, the function `time.strftime()` formats the current time (obtained using `time.localtime()`) as a string, using a specified format. The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.

## Conclusion
The `time` module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and `time` conversions. Whether you are writing a script, a library, or an application, the `time` module is a powerful tool that can help you perform time-related tasks with ease and efficiency. So, if you haven't already, be sure to check out the time module in Python and see how it can help you write better, more efficient code.

# Day 85 - Creating Command Line Utilities in Python
Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in `argparse` module.

## Syntax
Here is the basic syntax for creating a command line utility using `argparse` in Python:
```python
import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)
```
## Examples
Here are a few examples to help you get started with creating command line utilities in Python:

### Adding optional arguments
The following example shows how to add an optional argument to your command line utility:
```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")

args = parser.parse_args()

print(args.optional)
```
### Adding positional arguments
The following example shows how to add a positional argument to your command line utility:
```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("positional", help="description of positional argument")

args = parser.parse_args()

print(args.positional)
```
### Adding arguments with type
The following example shows how to add an argument with a specified type:
```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", type=int, help="description of integer argument")

args = parser.parse_args()

print(args.n)
```
## Conclusion
Creating command line utilities in Python is a straightforward and flexible process thanks to the `argparse` module. With a few lines of code, you can create powerful and customizable command line tools that can make your development workflow easier and more efficient. Whether you're working on small scripts or large applications, the `argparse` module is a must-have tool for any Python developer.

# Day 86 - The Walrus Operator in Python
The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

The Walrus Operator is represented by the `:=` syntax and can be used in a variety of contexts including while loops and if statements.

Here's an example of how you can use the Walrus Operator in a while loop:
```python
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
```
In this example, the length of the `numbers` list is assigned to the variable n using the Walrus Operator. The value of `n` is then used in the condition of the while loop, so that the loop will continue to execute until the `numbers` list is empty.

Another example of using the Walrus Operator in an if statement:
```python
names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")
```
Here is another example 
```python
# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
```
In this example, the user input is assigned to the variable `name` using the Walrus Operator. The value of `name` is then used in the if statement to determine whether it is in the names list. If it is, the corresponding message is printed, otherwise, a different message is printed.

It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.

In conclusion, the Walrus Operator is a useful tool for Python developers to have in their toolkit. It can help streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability.

# Day 87 - Shutil Module in Python
Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. In this repl, we'll take a closer look at the shutil module and its various functions and how they can be used in Python.

## Importing shutil
The syntax for importing the shutil module is as follows:
```python
import shutil
```

## Functions
The following are some of the most commonly used functions in the shutil module:

- `shutil.copy(src, dst)`: This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

- `shutil.copy2(src, dst)`: This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

- `shutil.copytree(src, dst)`: This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

- `shutil.move(src, dst)`: This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

- `shutil.rmtree(path)`: This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.

## Examples
Here are some examples of how you can use the shutil module in your Python code:

```python
import shutil

# Copying a file
shutil.copy("src.txt", "dst.txt")

# Copying a directory
shutil.copytree("src_dir", "dst_dir")

# Moving a file
shutil.move("src.txt", "dst.txt")

# Deleting a directory
shutil.rmtree("dir")
```
As you can see, the shutil module provides a simple and efficient way to perform common file and directory-related tasks in Python. Whether you need to copy, move, delete, or preserve metadata about files and directories, the shutil module has you covered.

In conclusion, the shutil module is a powerful tool for automating file and directory-related tasks in Python. Whether you are a beginner or an experienced Python developer, the shutil module is an essential tool to have in your toolbox.

# Day 88 - Exercise 9: Solution

[1067. Shoutouts to Everyone.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1067.%20Shoutouts%20to%20Everyone.py)

# Day 89 - Requests module in python
The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
## Installation 
```bash
pip install requests
```
## Get Request
Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:
```python
import requests
response = requests.get("https://www.google.com")
print(response.text)
```
## Post Request
Here is another example that sends a POST request to a web service and includes a custom header:
```python
import requests

url = "https://api.example.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
```

In this example, we send a POST request to a web service to authenticate a user. We include a custom User-Agent header and a JSON payload with the user's credentials.

## bs4 Module
There is another module called BeautifulSoup which is used for web scraping in Python. I have personally used bs4 module to finish a lot of freelancing task.

# Day 90 - Exercise 10: NEWS App

Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
Go to: https://newsapi.org/
and explore the various options to build you application

