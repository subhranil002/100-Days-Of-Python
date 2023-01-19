## Day 41 - If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:
```python
a = 2
b = 330
print("A") if a > b else print("B")
```

You can also have multiple else statements on the same line:

## Example
One line if else statement, with 3 conditions:
```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

## Another Example
```python
result = value_if_true if condition else value_if_false

```

This syntax is equivalent to the following if-else statement:
```python
if condition:
    result = value_if_true
else:
    result = value_if_false

```
## Conclusion
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition. \
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.

# Day 42 - Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:
```python
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

```

The output of this code will be:

```python
0 apple
1 banana
2 mango

```
As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.
# Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:


```python
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

```

This will output:
```python
1 apple
2 banana
3 mango

```

The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

```python
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

```
This will output:
```python
1: apple
2: banana
3: mango

```

In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:

```python
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

```
And here's an example with a string:
```python
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)

```

# Day 43 - Virtual Environment
A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

To create a virtual environment in Python, you can use the venv module that comes with Python. Here's an example of how to create a virtual environment and activate it:

```python
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate.bat
```
Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

To deactivate the virtual environment, you can use the deactivate command:
 ```python
# Deactivate the virtual environment
deactivate

```
## The "requirements.txt" file
In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:

```python
# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt
``` 
To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:

```python
# Install the packages listed in the requirements.txt file
pip install -r requirements.txt
```
Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.

# Day 44 - How importing in python works
Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

```python
import math
```
Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

```python
import math

result = math.sqrt(9)
print(result)  # Output: 3.0
```

## from keyword
You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:

```python
from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0
```
You can also import multiple functions or variables at once by separating them with a comma:

```python
from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```

## importing everything
It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.

```python
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```
Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

## The "as" keyword
```python
import math as m

result = m.sqrt(9)
print(result)  # Output: 3.0

print(m.pi)  # Output: 3.141592653589793
```
## The dir function
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

```python
import math

print(dir(math))
```
This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.

# Day 45 - `if "__name__ == "__main__"` in Python
The if `__name__ == "__main__"` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the `__name__` variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the `__name__` variable is set to the string `__main__` When the script is imported as a module into another script, the `__name__` variable is set to the name of the module.

Here's an example of how the if `__name__` == `__main__` idiom can be used:

```python
def main():
    # Code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__":
    main()
```
In this example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom checks whether the `__name__` variable is equal to `__main__`. If it is, the main function is called.
## Why is it useful?
This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script:

```python
def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
```
If you run this script directly, it will output "Running script directly". However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:

```python
import script

script.main()  # Output: "Running script directly"
```
This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.

## Is it a necessity?
It's important to note that the `if __name__ == "__main__"` idiom is not required to run a Python script. You can still run a script without it by simply calling the functions or running the code you want to execute directly. However, the `if __name__ == "__main__"` idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.

In summary, the `if __name__ == "__main__"` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.

# Day 46 - OS Module in Python
The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

Here are some common tasks you can perform with the os module:

Reading and writing files
The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:

```python
import os

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)
```
To open a file for writing, you can use the os.O_WRONLY flag:

```python
import os

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)
```
## Interacting with the file system
The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory:

```python
import os

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']
```
You can also use the os.mkdir function to create a new directory:

```python
import os

# Create a new directory
os.mkdir("newdir")
```
## Running system commands
Finally, the os module provides functions for running system commands. For example, you can use the os.system function to run a command and get the output:

```python
import os

# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
```
You can also use the os.popen function to run a command and get the output as a file-like object:

```python
import os

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()
```
In summary, the os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.

# Day 47 - Exercise 4: Solution

[1036. Secret Code Language.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1036.%20Secret%20Code%20Language.py)

# Day 48 - local and global variables
Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =. For example:
```python 
x = 5
y = "Hello, World!"

```

Now, let's talk about local and global variables.

A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

Here's an example to help clarify the difference:
```python
x = 10 # global variable

def my_function():
  y = 5 # local variable
  print(y)

my_function()
print(x)
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

```
In this example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function.
# The global keyword
Now, what if we want to modify a global variable from within a function? This is where the global keyword comes in.

The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. Here's an example:
```python 
x = 10 # global variable

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable

my_function()
print(x) # prints 5
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

```

In this example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

# Day 49 - File IO
Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.
## Opening a File
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:
```python
f = open('myfile.txt', 'r')
```
By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.
## Modes in file
There are various modes in which we can open files.

1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
4. create (x): This mode creates a file and gives an error if the file already exists.
 
5. text (t): 
Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
6. binary (b): used to handle binary files (images, pdfs, etc).
## Reading from a File
Once we have a file object, we can use various methods to read from the file.

The read() method reads the entire contents of the file and returns it as a string.
```python 
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
```


## Writing to a File
To write to a file, we first need to open it in write mode.
```python
f = open('myfile.txt', 'w')

```
We can then use the write() method to write to the file.
```python
f = open('myfile.txt', 'w')
f.write('Hello, world!')

```
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

```python 
f = open('myfile.txt', 'a')
f.write('Hello, world!')
```
## Closing a File
It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

To close a file, you can use the close() method.
```python 
f = open('myfile.txt', 'r')
# ... do something with the file
f.close()

```
## The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.

```python
with open('myfile.txt', 'r') as f:
    # ... do something with the file

```
# Day 50 - Readline, Writelines
## readlines() method
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

```python
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

```
The readlines() method reads all the lines of the file and returns them as a list of strings.

## writelines() method
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:
```python
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
```
This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:
```python
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
```
It is also a good practice to close the file after you are done with it.
