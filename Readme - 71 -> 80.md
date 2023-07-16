# Day 71 - `dir()`, `__dict__` and `help()` methods in python
We must look into `dir()`,  `__dict__()` and `help()` attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. 
In Python, there are three built-in functions that are commonly used to get information about objects: dir(), __dict__, and help(). Let's take a look at each of them:
## The `dir()` method
`dir()`: The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
Example:

```python
>>> x = [1, 2, 3]
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## The `__dict__` attribute
``__dict__``: The `__dict__` attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
Example:

```python
>>> class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>> p = Person("John", 30)
>>> p.__dict__
```
### Output
```
{'name': 'John', 'age': 30}
```
## The help() mehthod
`help()`: The help() function is used to get help documentation for an object, including a description of its attributes and methods.
Example:

```python
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
   ```
In conclusion, dir(), __dict__, and help() are useful built-in functions in Python that can be used to get information about objects. They are valuable tools for introspection and discovery.

# Day 72 - Super keyword in Python 
The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.


Here's an example of how to use the super() keyword in a simple inheritance scenario:

```python
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
```
## Output:

```python 
This is the child method.
This is the parent method.
  ```
In this example, we have a ParentClass with a parent_method and a ChildClass that inherits from ParentClass and overrides the child_method. When the child_method is called, it first prints "This is the child method." and then calls the parent_method using the super() keyword.

The super() keyword is also useful when a class inherits from multiple parent classes. In this case, you can specify the parent class from which you want to call the method.

Here's an example:

```python
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
```
### Output:
```python 
This is the child method.
This is the parent method of ParentClass1.
```
In this example, the ChildClass inherits from both ParentClass1 and ParentClass2. The child_method calls the parent_method of the first parent class using the super() keyword.

In conclusion, the super() keyword is a useful tool in Python when you want to call a parent class method in a child class. It can be used in inheritance scenarios with a single parent class or multiple parent classes.

# Day 73 - Magic/Dunder Methods in Python
These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

Let’s take a look at some of the most commonly used magic methods in Python.
## `__init__ method`
The __init__ method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need.
Also called "constructor", we have discussed this method already
## `__str__ and __repr__ methods`
The __str__ and __repr__ methods are both used to convert an object to a string representation. The __str__ method is used when you want to print out an object, while the __repr__ method is used when you want to get a string representation of an object that can be used to recreate the object.
## `__len__ method`

The __len__ method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.


## `__call__ method`
The __call__ method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand. So if you’re looking for a way to take your Python code to the next level, take some time to learn about these magic methods.

# Day 74 - Method Overriding in Python

Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

In Python, method overriding is a way to customize the behavior of a class based on its specific needs. For example, consider the following base class:

```python
class Shape:
    def area(self):
        pass
```
In this base class, the area method is defined, but does not have any implementation. If you want to create a derived class that represents a circle, you can override the area method and provide an implementation that calculates the area of a circle:

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```
In this example, the Circle class inherits from the Shape class, and overrides the area method. The new implementation of the area method calculates the area of a circle, based on its radius.

It's important to note that when you override a method, the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same.

Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, you can use the super function. The super function allows you to call the base class method from the derived class method, and can be useful when you want to extend the behavior of the base class method, rather than replace it.

For example, consider the following base class:

```python
class Shape:
    def area(self):
        print("Calculating area...")
```
In this base class, the area method prints a message indicating that the area is being calculated. If you want to create a derived class that represents a circle, and you also want to print a message indicating the type of shape, you can use the super function to call the base class method, and add your own message:

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius
```
In this example, the Circle class overrides the area method, and calls the base class method using the super function. This allows you to extend the behavior of the base class method, while still maintaining its original behavior.

In conclusion, method overriding is a powerful feature in Python that allows you to customize the behavior of a class based on its specific needs. By using method overriding, you can create more robust and reliable code, and ensure that your classes behave in the way that you need them to. Additionally, by using the super function, you can extend the behavior of a base class method, rather than replace it, giving you even greater flexibility and control over the behavior of your classes.

# Day 75 - Exercise 7: Solution

[1054. Clear the Clutter.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1054.%20Clear%20the%20Clutter.py)

# Day 76 - Exercise 8: Merge the PDF

Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

# Day 77 - Operator Overloading in Python: An Introduction

Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

## Why do we need operator overloading?

Operator overloading allows you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:

```python
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6
```

### How to overload an operator in Python?

You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:
```
+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__
```
For example, if you want to overload the + operator to add two instances of a custom class, you would define the __add__ method:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```
It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.

## Conclusion

Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code. By redefining the behavior of mathematical and comparison operators for custom data types, you can write code that is both concise and expressive. However, it's important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.

# Day 78 - Single Inheritance in Python
Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

## Syntax
The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this:

```python
class ChildClass(ParentClass):
    # class body

```

## Example
Let's consider a simple example of single inheritance in Python. Consider a class named "Animal" that contains the attributes and behaviors that are common to all animals.
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
```

If we want to create a new class for a specific type of animal, such as a dog, we can create a new class named "Dog" that inherits from the Animal class.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
```
The Dog class inherits all the attributes and behaviors of the Animal class, including the `__init__` method and the `make_sound` method. Additionally, the Dog class has its own `__init__` method that adds a new attribute for the breed of the dog, and it also overrides the `make_sound` method to specify the sound that a dog makes.


Single inheritance is a powerful tool in Python that allows you to create new classes based on existing classes. It allows you to reuse code, extend it to fit your needs, and make it easier to manage complex systems. Understanding single inheritance is an important step in becoming proficient in object-oriented programming in Python.

# Day 79 - Multiple Inheritance in Python
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.


## Syntax
In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.
```python
class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body
```

In this example, the `ChildClass` inherits attributes and methods from all three parent classes: `ParentClass1`, `ParentClass2`, and `ParentClass3`.

It's important to note that, in case of multiple inheritance, Python follows a `method resolution order (MRO)` to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods. 

## Example
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
```
In this example, the `Dog` class inherits from both the `Animal` and `Mammal` classes, so it can use attributes and methods from both parent classes.

# Day 80 - Multilevel Inheritance in Python
Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.

In Python, multilevel inheritance is achieved by using the class hierarchy. The syntax for multilevel inheritance is quite simple and follows the same syntax as single inheritance.

## Syntax
``` python
class BaseClass:
    # Base class code
    
class DerivedClass1(BaseClass):
    # Derived class 1 code
    
class DerivedClass2(DerivedClass1):
    # Derived class 2 code
```
In the above example, we have three classes: `BaseClass`, `DerivedClass1`, and `DerivedClass2`. The `DerivedClass1` class inherits from the `BaseClass`, and the `DerivedClass2` class inherits from the `DerivedClass1` class. This creates a hierarchy where `DerivedClass2` has access to all the attributes and methods of both `DerivedClass1` and `BaseClass`.

## Example
Let's take a look at an example to understand how multilevel inheritance works in Python. Consider the following classes:
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
```
In this example, we have three classes: `Animal`, `Dog`, and `GoldenRetriever`. The `Dog` class inherits from the `Animal` class, and the `GoldenRetriever` class inherits from the `Dog` class.

Now, when we create an object of the `GoldenRetriever` class, it has access to all the attributes and methods of the `Animal` class and the `Dog` class. We can also see that the `GoldenRetriever` class has its own attributes and methods that are specific to the class.
```python
dog = GoldenRetriever("Max", "Golden")
dog.show_details()
```
### Output:
```
Name: Max
Species: Dog
Breed: Golden Retriever
Color: Golden
```
As we can see from the output, the `GoldenRetriever` object has access to all the attributes and methods of the `Animal` and `Dog` classes, and, it has also added its own unique attributes and methods. This is a powerful feature of multilevel inheritance, as it allows you to create more complex and intricate classes by building upon existing ones.

Another important aspect of multilevel inheritance is that it allows you to reuse code and avoid repeating the same logic multiple times. This can lead to better maintainability and readability of your code, as you can abstract away complex logic into base classes and build upon them.

In conclusion, multilevel inheritance is a powerful feature in object-oriented programming that allows you to create complex and intricate classes by building upon existing ones. It provides the benefits of code reuse, maintainability, and readability, while also requiring careful consideration to avoid potential problems.


