def my_generator():
    for i in range(5):
        # Complex computations
        yield i


gen = my_generator()

# print(next(gen)) # 0
# print(next(gen)) # 1
# print(next(gen)) # 2

for j in gen:
    print(j) # 0 1 2 3 4 