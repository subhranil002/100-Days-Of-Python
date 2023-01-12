info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) # {'name': 'Karan', 'age': 19, 'eligible': True}
info.update({'age':20})
info.update({'DOB':2001})
print(info) # {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info) # {}

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info) # {'name': 'Karan', 'age': 19}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info) # {'name': 'Karan', 'age': 19, 'eligible': True}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info) # {'name': 'Karan', 'eligible': True, 'DOB': 2003}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info) # Error