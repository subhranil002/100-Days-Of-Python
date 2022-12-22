x = int(input("Enter value :"))
# x is the variable to match
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _:
        print("Default Statement")