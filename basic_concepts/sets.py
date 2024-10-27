#sets are unordered, unchangeables, unindexed and do not allow duplicate values
# since sets are unodered so you can not be sure in which order the items will appear.
# once the set has been created you can not change its items, but you can add new items.

colors = {'red', 'blue', 'green'}

print(colors)


#len()
print (len(colors))

#set can be of any type and contain different types.
demographic_data = {'Jhon', 'Smith', 45, 'Canada', True, 'Engineer'}
print(demographic_data)

#create sets using the set class's constructor
countries = set(('Panama', 'USA', 'China'))
print(countries)

#Access Set's items
for item in countries:
    print (item)

#Check if an items is found in the Set
if 'Panama' in countries:
    print('Found!')

print('USA' in countries) #prints True if finds the item.



#add(): add items
countries.add('Isrrael')
print(countries)


#update() : Join sets
countries.update(colors)
print(countries)

#union(): you can also join Sets by using the union method. this method returns a new Set
new_set = colors.union(countries)
print(new_set)

#Both union and update will exclude any dublicate value.

#intersection_udpate() : to keep only the dublicate values
new_set.intersection_update(colors)
print(new_set)

#symmetric_difference_update() : to keep only the elements that are not present in both sets.
new_set.symmetric_difference_update(colors)
print(new_set)

#symmetric_difference() : to keep return a new Set containing only the elements that are not present in both sets.
another_new_set = new_set.symmetric_difference(colors)
print(another_new_set)

#update(): add new iterable.
#the object is the method does have to be a set.  it can be any iterable object (tuples, lists, dictionaries, etc)
countries.update(['Spain', 'Mexico'])
print(countries)


#Remove Set's items
#you can use the remove or discard methods. if the items to remove is not found remove() will aise an error but discard() will not raise an error.
countries.remove('Panama')
colors.discard('red')
print(countries)
print(colors)

#you can also use pop() to remove an item. however this method will always remove the last item because this Sets are not indexed, and since they are nos ordered you don't know which element is actually going to be removed.
removed_el = countries.pop()
print(removed_el)
print(countries)

#clear(): clear methos empties the set
colors.clear()
print(colors)

#del keyword: this key word will delete the set completely
del colors


#....... Looping the sets
# for loop
animals = {'cat', 'dog', 'tiger', 'lion'}
for animal in animals:
    print(animal)
    

#issuperset()	Returns whether this set contains another set or not
#issubset()	Returns whether another set contains this set or not
#isdisjoint()	Returns whether two sets have a intersection or not
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set