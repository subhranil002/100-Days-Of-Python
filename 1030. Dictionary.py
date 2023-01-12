info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) # {'name': 'Karan', 'age': 19, 'eligible': True}
print(type(info)) # <class 'dict'>

dic = {
    344: "Harry",
    345: "Subhranil",
    346: "Others"
}
print(dic[345]) # Subhranil
# print(dic[335]) # Error

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name']) # Karan
print(info.get('name')) # Karan
# print(info('name1')) # Error
print(info.get('name1')) # None

for key in info.keys():
    print(info[key],end=" ") # Karan 19 True 
print("\n")

print(info.items()) # dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])