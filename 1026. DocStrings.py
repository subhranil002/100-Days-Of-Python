def square(n):
    '''Takes in a number n, returns the square of n''' # Initiating DocString
    print(n**2) # 25
square(5)

print(square.__doc__) # Takes in a number n, returns the square of n

def square(n):
    print(":)") # :)
    '''Takes in a number n, returns the square of n''' # Initiating DocString
    print(n**2) # 25
square(5)

print(square.__doc__) # None
