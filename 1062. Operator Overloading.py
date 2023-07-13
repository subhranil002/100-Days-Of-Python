class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vector(self.i + x.i,  self.j+x.j, self.k+x.k)


v1 = Vector(3, 5, 6)
print(v1)  # 3i + 5j + 6k

v2 = Vector(1, 2, 9)
print(v2)  # 1i + 2j + 9k

print(v1 + v2) # 4i + 7j + 15k