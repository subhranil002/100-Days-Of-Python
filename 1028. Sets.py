s = {2, 4, 2, 6} # Initiating a Set 
# (Unchangeable,Dosen't repeats same value)
print(type(s)) # <class 'set'>
print(s) # {2, 4, 6}

info = {"Carla", 19, False, 5.9, 19}
print(info) # {False, 19, 'Carla', 5.9}
# Doesn't maintains a order

# How to make a empty set -->
st = {} # Wrong
print(type(st)) # <class 'dict'>
st = set() # Right
print(type(st)) # <class 'set'>