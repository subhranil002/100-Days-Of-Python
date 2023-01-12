cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3) # {'Seoul', 'Tokyo', 'Berlin', 'Delhi', 'Madrid', 'Kabul'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3) # {'Tokyo', 'Madrid'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities) #{'Delhi', 'Berlin', 'Tokyo', 'Kabul', 'Madrid', 'Seoul'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities) # {'Madrid', 'Tokyo'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3) # {'Delhi', 'Seoul', 'Berlin', 'Kabul'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities) # {'Delhi', 'Seoul', 'Berlin', 'Kabul'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3) # {'Madrid', 'Tokyo', 'Berlin'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2)) # False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2)) # False
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3)) # False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities)) # True

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities) # {'Berlin', 'Madrid', 'Delhi', 'Helsinki', 'Tokyo'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities) # {'Berlin', 'Madrid', 'Delhi'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities) # {'Berlin', 'Delhi', 'Tokyo'}
print(item) # Madrid

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) # Will Throw Error

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities) # set()