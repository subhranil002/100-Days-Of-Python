class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):  # Don't need "self"
        return a + b


a = Math(5)

print(a.num)  # 5

a.addtonum(6)

print(a.num)  # 11

print(a.add(7, 2)) # 9
