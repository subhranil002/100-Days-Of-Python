def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 5; 
print("Number :",num)
print("Factorial :",factorial(num))


def fibonacci (n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Driver Code 
for i in range(10):
    print(fibonacci(i))