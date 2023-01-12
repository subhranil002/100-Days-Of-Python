# Syntax -->
# try:
#     statements which could generate 
#     exception
# except:
#     solution of generated exception
# finally:
#     block of code which is going to 
#     execute in any situation

try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index :"))
    print(l[i])
except:
    print("Some Error Occurred")
finally:
    print("I am Always Executed")
    
# Output 1 -->
# Enter the index :2
# 6
# I am Always Executed

# Output 2 -->
# Enter the index :5
# Some Error Occurred 
# I am Always Executed