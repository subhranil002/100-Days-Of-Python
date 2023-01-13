# Syntax for custom error -->
a = int(input("Enter value between 5 and 9 :"))
if (a<5 or a>9):
    raise ValueError("Value Should be between 5 and 9")


# Syntax for custom exception -->
# class CustomError(Exception):
#     code ...
#     pass

# try:
#     code ...

# except CustomError:
#     code...