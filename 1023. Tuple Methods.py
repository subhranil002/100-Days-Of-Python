numbers1 = (1, 2, 3, 4, 5, 6)
print(numbers1) # (1, 2, 3, 4, 5, 6)
print(type(numbers1)) # <class 'tuple'>
# To Edit -->

temp = list(numbers1)
print(type(temp)) # <class 'list'>
temp.append(7)
temp[2] = 0
numbers2 = tuple(temp)
print(numbers2) # (1, 2, 0, 4, 5, 6, 7)
print(type(numbers2)) # <class 'tuple'>