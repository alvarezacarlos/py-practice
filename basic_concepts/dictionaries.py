# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

student = {
    'name': 'Jhon',
    'lastname': 'Smith',
    'age': 15,
    'subjects': ['Math', 'Spanish', 'Phisics']
}

print(student)

# Acccess a dictionary
print(student['age'])
print(student['lastname'])
print(student['name'])
print(student['subjects'])

print(student['subjects'])
print(student['subjects'][0])
print(student['subjects'][1])
print(student['subjects'][2])

# get(): we can also access the dictionary properties with get()
print(student.get('subjects'))

#print the number of tems in the dictionary
print(len(student))

#keys() : this method returns the dictionary's keys
print(student.keys())

#values() : this method returns the list of values in the dictionary
print(student.values())

#items(): the items() till return each item in a dictinary
print(student.items())

#check if key exists in the dictinary
if 'name' in student:
    print('Found!')
    
#Update an items in the dictionary
student['name'] = 'Laura'
print(student)

#update() method. 
student.update({'lastname': 'Brown'})
print(student)

#adding an item to a dictionary 
student['country'] = 'Panama'
print(student)

#Remove an item from a dictionary with pop()
student.pop('country')
print(student)

#popitem() : this method removes the last items inserted in the dictionary
student.popitem()
print(student)

#del keyword : this keyword removes the item with the specified key name.
del student['age']
print(student)

#clear() : this method remove all the properties of the dictionary
student.clear()
print(student)

#del keyword: this ord can also delete the dictionary completely
del student


#Loop dictionary
teacher = {
    'name': 'Jhon',
    'lastname': 'Smith',
    'age': 40,
    'subjects': ['Math', 'Spanish', 'Phisics']
}

#for Loop
for item in teacher:
    print(teacher[item])
    
#values() you can also use the values() method to return the values
for value in teacher.values():
    print(value)
    
#keys() you can also use the keys() method to return the keys
for key in teacher.keys():
    print(key)

#items(): this method allows to loop trough both the keys and values of the dictionary
for key, value in teacher.items():
    print(key + ' : ' + str(value))
    

#Copy dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#copy():  one way is to use the built-in Dictionary method copy().
professor = teacher.copy()
print(professor)

#dict(): this method also allows us to copy a dictionary
tutor = dict(professor)
print(tutor)

#Nested dictionary
child1 = {
  "name" : "Jhon",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily['child1'])
print(myfamily['child1']['name'])

child4 = {
  "name" : "Marcos",
  "year" : 2021
}

#setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
myfamily.setdefault('child4', child4)

print(myfamily)

#fromkeys() Returns a dictionary with the specified keys and value
keys = ('name', 'age', 'country')
value = 45
person = dict.fromkeys(keys, value)
print(person)
