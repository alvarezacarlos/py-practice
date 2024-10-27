# A tuple is a collection which is ordered meaning that each item has an order and it will not change  and unchangeable meaning that we can not change, add or remove items after the tubles has beed created..
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

colors = ('green', 'blue', 'red', 'black')
print(colors)


#since tuples are indexed they can have items with the same value.
countries = ('Panama', 'USA', 'Canada', 'Panama', 'USA')
print(countries)


#Create a tuple with one item.
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
visited_countries = ('China', )
print(visited_countries)


#tuples can contain any and different data types mixed.
demographic_data = ('Jhon', 'Smith', 45, 'Canada', True, 'Engineer')
print(demographic_data)

#tuple is just an object which is an instance of the class tuple. so we can create a tuple by calling the tuple class constructor.
numbers = tuple((1, 2, 3, 4, 5, 6))
print(numbers)


#............ Access Tuple 
print(countries[4])
print(countries[0:2]) #range: index 2 is not included


# find an item in the list
if 'Canada' in countries:
    print('Found!')
    
#................ workarounds to alter tuples
#update a tuple items
#Tuples are unchangeble or immutable, meaning we can not change, add or remove items once the tuple is created. But there are some work around. We can convert the tuple into a list to modify the list and set the previous tuple to the modified list converted to tuple.
demographic_data_list = list(demographic_data)
demographic_data_list[0] = 'Peter'
demographic_data = tuple(demographic_data_list)
print(demographic_data)

#add items
#we can also convert the tuple into a list to then add items and finally update it with the list converted to tuple.
demographic_data_list2 = list(demographic_data)
demographic_data_list2.append('Male')
demographic_data = tuple(demographic_data_list2)
print(demographic_data)


#Add tuple to a tuple
demographic_data += visited_countries
print(demographic_data)

#remove items
#to remove items we have to perform the convertion to list and remove the item as well.
demographic_data_list3 = list(demographic_data)
demographic_data_list3.pop(1)
demographic_data = tuple(demographic_data_list3)
print(demographic_data)


#unpacking a tuple: the number of variables must match the number of value sin he tuple. if not, you must use the asterisk to collect the remaining values as a list.
(green, blue, red, black) = colors
print(green, blue, red, black)

(green_color, blue_color, *other_colors) = colors
print(other_colors)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
(first_color, *some_colors, red_color, black_color) = colors
print(first_color)
print(some_colors)
print(red_color)
print(black_color)

(country,) = visited_countries
print(country)

#.................Loop
#using a for loop
for color in colors:
    print(color)

#range() : you can also loop through a tuple items by referring to their index number.
for i in range(len(colors)):
    print(colors[i])
    
#while Loop
i = 0
while i < len(colors):
    print(colors[i])
    i += 1
        
#Join Tuples
# + operator
combined_tuples = colors + visited_countries
print(combined_tuples)

#multiply items of a tuple. this extends the same list the times we indicate it.
print(numbers)
multiplied_numbers = numbers * 5
print(multiplied_numbers)

#count(): return the number of times an items is found in a tuple
#index(): return the index of a specified value. it return the first occurance.