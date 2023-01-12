# Syntax -->
# try:
#     statements which could generate 
#     exception
# except:
#     Soloution of generated exception

a = input("Enter the number :")
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,10):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid Input")
    
print("Some imp line of code")
print("End of Program")

# Output 1 -->
# Enter the number :4
# Multiplication table of 4 is :
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# Some imp line of code
# End of Program

# Output 2 -->
# Enter the number :Subhranil
# Multiplication table of Subhranil is :invalid literal for int() with base 10: 'Subhranil'
# Invalid Input
# Some imp line of code
# End of Program