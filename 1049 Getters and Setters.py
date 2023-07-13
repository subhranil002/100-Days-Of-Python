class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
        return 10 * self._value


obj = MyClass(10)
obj.show() # Value is 10

# Without Setter

# obj.ten_value = 67
# print(obj.ten_value) # AttributeError: property 'ten_value' of 'MyClass' object has no setter

# With Setter

obj.ten_value = 67
print(obj.ten_value) # 67.0

obj.show()  # Value is 6.7
