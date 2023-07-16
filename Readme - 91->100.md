# Day 91 - Generators in Python
Generators in Python are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

## Creating a Generator
In Python, you can create a generator by using the `yield` statement in a function. The `yield` statement returns a value from the generator and suspends the execution of the function until the next value is requested. Here's an example:
```python
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Output:
# 0
# 1
# 2
# 3
# 4
```
As you can see, the generator function `my_generator()` returns a generator object, which can be used to generate the values in the range 0 to 4. The `next()` function is used to request the next value from the generator, and the generator resumes its execution until it encounters another `yield` statement or until it reaches the end of the function.

## Using a Generator
Once you have created a generator, you can use it in a variety of ways, such as in a for loop, a list comprehension, or a generator expression. Here's an example:
```python
gen = my_generator()
for i in gen:
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```
As you can see, the generator can be used in a for loop, just like any other iterable sequence. The generator is used to generate the values one-by-one as the loop iterates over it.

## Benefits of Generators
Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.

## Conclusion
Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit. So, if you haven't already, be sure to check out generators in Python and see how they can help you write better, more efficient code.

# Day 92 - Function Caching in Python 
Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called. Here's an example:

```python
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
# Output: 6765
```
As you can see, the `functools.lru_cache` decorator is used to cache the results of the `fib` function. The `maxsize` parameter is used to specify the maximum number of results to cache. If `maxsize` is set to `None`, the cache will have an unlimited size.

## Benefits of Function Caching
Function caching can have a significant impact on the performance of a program, particularly for computationally expensive functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources.

Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a function. With the `functools.lru_cache` decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.

## Conclusion
Function caching is a technique for improving the performance of a program by storing the results of a function so that you can reuse the results instead of recomputing them every time the function is called. In Python 3, function caching can be achieved using the `functools.lru_cache` decorator, which provides an easy and efficient way to cache the results of a function. Whether you're writing a computationally expensive program, or just want to simplify your code, function caching is a great technique to have in your toolbox.

# Day 93 - Exercise 10: Solution

[1073. NEWS App.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1073.%20NEWS%20App.py)

# Day 94 - Exercise 11: Drink Water Reminder

Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

# Day 95 - Regular Expressions in Python
Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.
## Metacharacters in regular expressions
``` 
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
```
Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
## Importing re Package
In Python, regular expressions are supported by the `re` module. The basic syntax for working with regular expressions in Python is as follows:

```python
import re
```

## Searching for a pattern in re using re.search() Method
re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.
We can use re.search method like this to search for a pattern in regular expression:
```python
# Define a regular expression pattern
pattern = r"expression"

# Match the pattern against a string
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
```
## Searching for a pattern in re using re.findall() Method
You can also use the `re.findall` function to find all occurrences of the pattern in a string:


```python
import re
pattern = r"expression"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']
```

### Replacing a pattern
The following example shows how to replace a pattern in a string:
```python
import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)

print(new_text)
# Output: "The dog is in the dog."
```

### Extracting information from a string
The following example shows how to extract information from a string using regular expressions:

```python
import re

text = "The email address is example@example.com."

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)
# Output: example@example.com
```
## Conclusion
Regular expressions are a powerful tool for working with strings and text data in Python. Whether you're matching patterns, replacing text, or extracting information, regular expressions make it easy to perform complex string operations with just a few lines of code. With a little bit of practice, you'll be able to use regular expressions to solve all sorts of string-related problems in Python.

# Day 96 - Async IO in Python
Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the `asyncio` module and asynchronous functions.

## Syntax
Here is the basic syntax for creating an asynchronous function in Python:
```python
import asyncio

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())
```

Another way to schedule tasks concurrently is as follows: 
``` python  
L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
print(L)
```
Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the `asyncio` module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.

# Day 97 - Multithreading in Python

Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.

## Importing Threading
We can use threading by importing the threading module.

```python
import threading
```

## Creating a thread
To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method. Here's how we can create a simple thread.

```python
import threading
def my_func():
  print("Hello from thread", threading.current_thread().name)
  thread = threading.Thread(target=my_func)
  thread.start()
  thread.join()
```
## Functions
The following are some of the most commonly used functions in the threading module:

- `threading.Thread(target, args)`: This function creates a new thread that runs the target function with the specified arguments.

- `threading.Lock()`: This function creates a lock that can be used to synchronize access to shared resources between threads.

## Creating multiple threads
Creating multiple threads is a common approach to using multithreading in Python. The idea is to create a pool of worker threads and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process tasks in parallel.

```python
import threading

def thread_task(task):
    # Do some work here
    print("Task processed:", task)

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    threads = []
    for task in tasks:
        thread = threading.Thread(target=thread_task, args=(task,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
```

## Using a lock to synchronize access to shared resources
When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads. A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code. The lock is released when the thread finishes executing the critical section.

```python
import threading

def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()

if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()

    threads = []
    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Counter value:", counter)
```

## Conclusion
As you can see, the threading module provides a simple and efficient way to implement multithreading in Python. Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources, the threading module has you covered.

In conclusion, the threading module is a powerful tool for parallelizing code in Python. Whether you are a beginner or an experienced Python developer, the threading module is an essential tool to have in your toolbox. With multithreading, you can take advantage of multiple CPU cores and significantly improve the performance of your code.

# Day 98 - Multiprocessing in Python
Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. In this repl, we'll take a closer look at the multiprocessing module and its various functions and how they can be used in Python.

## Importing Multiprocessing
We can use multiprocessing by importing the multiprocessing module. 

```python 
import multiprocessing
```

Now, to use multiprocessing we need to create a `process object` which calls a `start()` method. The start() method runs the process and then to stop the execution, we use the `join()` method. Here's how we can create a simple process.

## Creating a process
```python
import multiprocessing
def my_func():
  print("Hello from process", multiprocessing.current_process().name)
  process = multiprocessing.Process(target=my_func)
  process.start()
  process.join()
```
## Functions
The following are some of the most commonly used functions in the multiprocessing module:

- `multiprocessing.Process(target, args)`: This function creates a new process that runs the target function with the specified arguments.

- `multiprocessing.Pool(processes)`: This function creates a pool of worker processes that can be used to parallelize the execution of a function across multiple input values.

- `multiprocessing.Queue()`: This function creates a queue that can be used to communicate data between processes.

- `multiprocessing.Lock()`: This function creates a lock that can be used to synchronize access to shared resources between processes.

## Creating a pool of worker processes
Creating a pool of worker processes is a common approach to using multiprocessing in Python. The idea is to create a pool of worker processes and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process tasks in parallel.

```python
from multiprocessing import Pool

def process_task(task):
    # Do some work here
    print("Task processed:", task)

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)
```
## Using a queue to communicate between processes
When working with multiple processes, it is often necessary to pass data between them. One way to do this is by using a queue. A queue is a data structure that allows data to be inserted at one end and removed from the other end. In the context of multiprocessing, a queue can be used to pass data between processes.

```python
def producer(queue):
    for i in range(10):
        queue.put(i)


def consumer(queue):
    while True:
        item = queue.get()
        print(item)


queue = multiprocessing.Queue()
p1 = multiprocessing.Process(target=producer, args=(queue,))
p2 = multiprocessing.Process(target=consumer, args=(queue,))
p1.start()
p2.start()
```
## Using a lock to synchronize access to shared resources
When working with multiprocessing in python, locks can be used to synchronize access to shared resources among multiple processes. A lock is an object that acts as a semaphore, allowing only one process at a time to execute a critical section of code. The lock is released when the process finishes executing the critical section.

```python
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Counter value:", counter.value)
```

## Conclusion
As you can see, the multiprocessing module provides a simple and efficient way to run multiple processes in parallel. Whether you need to create a new process, run a function across multiple input values, communicate data between processes, or synchronize access to shared resources, the multiprocessing module has you covered.

In conclusion, the multiprocessing module is a powerful tool for parallelizing code in Python. Whether you are a beginner or an experienced Python developer, the multiprocessing module is an essential tool to have in your toolbox.

# Day 99 - Exercise 11: Solution

[1076. Drink Water Reminder.py](https://github.com/subhranil002/100-Days-Of-Python/blob/master/1076.%20Drink%20Water%20Reminder.py)

# Day 100 - Conclusion: Where to go from here

# Conclusion
Congratulations on completing the 100 days of Python code challenge! You have likely gained a solid foundation in the language and developed a range of skills, from basic syntax to more advanced concepts such as object-oriented programming. However, this is just the beginning of your journey with Python. There are many more topics to explore, including machine learning, web development, game development, and more.

## Where to go from here:
To continue your learning journey, consider exploring the following resources:

- Python books: There are many excellent books on Python that can help you deepen your knowledge and skills. Some popular options include "Python Crash Course" by Eric Matthes, "Automate the Boring Stuff with Python" by Al Sweigart, and "Fluent Python" by Luciano Ramalho. I would also like to recommend "Hands on Machine Learning book by Aurélien Géron"

- YouTube Projects: There are many YouTube projects available which can be watched after you have some basic understanding of python

- Python communities: There are many online communities where you can connect with other Python learners and experts, ask questions, and share your knowledge. Some popular options include the Python subreddit, the Python Discord server, and the Python community on Stack Overflow.

- GitHub repositories: GitHub is a great resource for finding Python projects, libraries, and code snippets. Some useful repositories to check out include "awesome-python" (a curated list of Python resources), "scikit-learn" (a machine learning library), and "django" (a web development framework).



Overall, the key to mastering Python (or any programming language) is to keep practicing and experimenting. Set yourself challenges, work on personal projects, and stay curious. Good luck!

