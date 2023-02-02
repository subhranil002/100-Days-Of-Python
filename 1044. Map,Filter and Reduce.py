def cube(x):
    return x*x*x

# Old Technique -->
# l = [1, 2, 3, 4, 5]
# newl = []
# for item in l:
#     newl.append(cube(item))
    
# print(newl) # [1, 8, 27, 64, 125]

# Introducing MAP -->
l = [1, 2, 3, 4, 5]
newl = list(map(cube, l))
print(newl) # [1, 8, 27, 64, 125]


# Introducing FILTER -->
l = [1, 22, 33, 4, 1.5]
def filter_function(a):
    return a>4 

newnewl = list(filter(filter_function, l))
print(newnewl) # [22, 33]

# Introducing REDUCE -->
from functools import reduce

def mysum(x, y):
    return x+y

numbers = [1, 2, 3, 4, 5]
sum = reduce(mysum, numbers)
print(sum) # 15 