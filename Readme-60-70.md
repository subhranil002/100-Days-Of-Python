# Day 61 - Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
## Python Inheritance Syntax
```python
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
  ```
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
## Types of inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

We will see the explaination and example of each type of inheritance in the later tutorials

# Day 62 - Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:
## Types of access specifiers 
1.  Public access modifier
2. Private access modifier
3. Protected access modifier

## Public Access Specifier in Python
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
### Example:
```python
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
```
### Output:
```
21
Harry
```
## Private Access Modifier
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.


In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
### Example:
```python
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())
```
### Output:
```
AttributeError: 'student' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
AttributeError: 'subject' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
```
Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

### Name mangling
Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

```python
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
```
In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute
   
# Day 63 - Exercise 5: Solution

[1045. Stone Paper Scissor.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1045.%20Stone%20Paper%20Scissor.py)

# Day 64 - Exercise 6: Library Management System

Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how  you can print all books, add a book and get the number of books using  different methods. Show that your program doesnt persist the books after the program is stopped!

# Day 65 - Static Methods

Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3
```
In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.

# Day 66 - Instance vs class variables
In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

## Class Variables
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.
```python
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2

```

In the example above, the class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable.

## Instance Variables
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the __init__ method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
```python
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane
```

In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.

## Summary
In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in Python.

It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name. But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.

# Day 67 - Exercise 6: Solution

[1052. Library Management System.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1052.%20Library%20Management%20System.py)

# Day 69 - Python Class Methods
## Python Class Methods: An Introduction

In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method." In this blog post, we will explore what Python class methods are, why they are useful, and how to use them.

## What are Python Class Methods?

A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

## Why Use Python Class Methods?

Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

## How to Use Python Class Methods

To define a class method, you simply use the "@classmethod" decorator before the method definition. The first argument of the method should always be "cls," which represents the class itself. Here is an example of how to define a class method:
```python
class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
```

In this example, the "factory_method" is a class method that takes two arguments, "argument1" and "argument2." It creates a new instance of the class "ExampleClass" using the "cls" keyword, and returns the new instance to the caller.

It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.

## Conclusion

Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.

# Day 70 - Class Methods as Alternative Constructors

In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

But what if you want to create a Person object from a string that contains the person's name and age, separated by a comma? You can define a class method named "from_string" to do this:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
```
Now you can create a Person object from a string like this:
```python 
person = Person.from_string("John Doe, 30")
```

Another common use case for class methods as alternative constructors is when you want to create an object with a different set of default values than what is provided by the default constructor. For example, consider a class named "Rectangle" that has two attributes: "width" and "height". The default constructor for the class might look like this:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

```
But what if you want to create a Rectangle object with a default width of 10 and a default height of 5? You can define a class method named "square" to do this:
```python
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  @classmethod
  def square(cls, size):
    return cls(size, size)
```
Now you can create a square rectangle like this:

```python
rectangle = Rectangle.square(10)
```


