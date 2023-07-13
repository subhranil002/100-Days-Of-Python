# Method for without arguments functions

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx


# @greet
# def hello():
#     print("Hello world")


# hello()
# # Good Morning
# # Hello world
# # Thanks for using this function


# Method for with arguments functions

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def add(a, b):
    print(a+b)


add(1, 2)
# Good Morning
# 3
# Thanks for using this function