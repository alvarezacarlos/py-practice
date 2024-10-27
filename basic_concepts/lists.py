colors = ['green', 'blue', 'black']

print(colors)

print()

print(colors[0], colors[1], colors[2])

print()

print(colors[1:3])

print()

print(len(colors))

#a list can contain different datatypes

person = ['Carlos', 25, 'Panama', 'Engineer']

print(person)


# Create a list using the list constructor. we can use the sonctructor since a list is an object to the class list. Then we can create a list using by creating an instance of the class list.
names = list(('Carlos', 'Marcos', 'Jhon'))

print(names)

#append
colors.append('orange')
print(colors)

#insert
names.insert(1,'Peter')
print(names)


#extend: To append elements from another list to the current list, use the extend() method.
names.extend(colors)
print(names)


#add any iterable
names.extend(['Mark', 'Skyblue', 46])
names.extend(('Paul', 'Purple', 100))
print(names)

#remove: remove the item value
names.remove('Mark')
names.remove('Paul')
print(names)

#pop: remove the item by passing the index. If you do not specify the index, the pop() method removes the last item.
names.pop(0)
print(names)
names.pop(0)
print(names)
names.pop(0)
print(names)
names.pop(0)
print(names)


#clear: The clear() method empties the list. The list still remains, but it has no content.
print(colors)
colors.clear()
print(colors)

#del: also removes the specified index:
del names[5]
print(names)


#del: the keyword del can also delte the completelist
del names
# print(names)  : output : name 'names' is not defined

#Loop
countries = ['Panama', 'USA', 'Colombia', 'China']
for country in countries:
    print(country)

for i, country in enumerate(countries):
    print(i, country)
    
#Loop with range: loop through the list items by referring to their index number.
for i in range(len(countries)):
    print(i, countries[i])

#looping with while
print('Print with While')
print('List lenth: {}'.format(len(countries)))
i = 0
while i < len(countries):
    print(i, countries[i])
    i+=1
 

#List Comprehension to print a list: List comprehension offers the shortest syntax for looping through lists   
[print(i, country) for i, country in enumerate(countries)]


#sort() : sorrt method to sort lists, it sorts the list Ascending by default.
print('Before sorting.....')
print(countries)
countries.sort()
print('After sorting.....')
print(countries)
print('Sorting descending')
countries.sort(reverse=True)
print(countries)

#sort() is case sensitive, it sort all the capital letters words before the lower case words. 
#To make it case-insensitive we use the next
my_family = ['Father', 'brother', 'Mother', 'sister', 'Son', 'daughter']
print('Case sensitve sort')
my_family.sort()
print(my_family)
print('Case insensitve sort')
my_family.sort(key = str.lower)
print(my_family)

#revrese the order of a list regardless of the alphabet
my_family.reverse()
print('Reverse the order of the list!')
print(my_family)


#............ copy a list .......
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

#copy(): there are ways to make a copy, one way is to use the built-in List method copy()
your_family = my_family.copy()
print(my_family)
print(your_family)

#we can also copy a list by using the built-in method list()
his_family = list(your_family)
print(his_family)

#.......... Join Lists ..........
#There are several ways to join or concatenate 2 or more lists.

# + operator
our_family = my_family + your_family
print(our_family)

#extend() : we can also use the extend methos which purpose is to add elements from one list to another list.
his_family.extend(my_family)
print(his_family)

#appen : we can also do an append of the lists
for i, item in enumerate(his_family):
    our_family.append(his_family[i])
print(our_family)


#count(): return the number of times an item appear in the list.
print(his_family.count('brother'))

#index(): return the position of a value, The index() method returns the position at the first occurrence of the specified value.
print(his_family.index('brother'))

#insert(): adds an element at the specified position.
his_family.insert(2,'Uncle')
print(his_family)

#pop(): removes an element at the specified position. it returned the removed element.
rem_El = his_family.pop(0)
print(his_family)
print(rem_El)

#remove(): remove the item with the specified value.
his_family.remove('Uncle')
print(his_family)