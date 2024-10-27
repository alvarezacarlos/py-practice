#an iterator is an object that contains a countable number off values.

#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:


#Return an iterator from a tuple, and print each value:
colors = ('green', 'red', 'blue', 'black')
my_iterator = iter(colors) 
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

#Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Looping Through an Iterator - We can also use a for loop to iterate through an iterable object: The for loop actually creates an iterator object and executes the next() method for each loop.
for color in colors:
    print(color)



#Object/Class Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar to the __init__() method, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    print('Hi from __iter__')
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    print('Hi from __next__')
    return x

myclass = MyNumbers()

# myclass.__iter__()
# print(myclass.a)

# myclass.__next__()
# print(myclass.a)
# myclass.__next__()
# print(myclass.a)
# myclass.__next__()
# print(myclass.a)
# myclass.__next__()
# print(myclass.a)
# myclass.__next__()
# print(myclass.a)
# myclass.__next__()
# print(myclass.a)


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
new_self_iterator = iter(myclass) #iter calls the __iter__() and returns a new self with the property a = 1
# print(myclass.a)
response = next(new_self_iterator) #next is returning the current a property value and incrementing the value in one.
print(response)
print(myclass.a)

response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)
response = next(new_self_iterator)
print(response)
print(myclass.a)

#StopIteration: to avoid the iteration to go on forever in a for loop for example, we can use the stop Iteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times.
class TestNumber:
    def __iter__(self):
        self.number = 1
        return self
    def __next__(self):
        if self.number <= 20:
            x = self.number
            self.number += 1
            return x
        else:
            raise StopIteration

myIterableClass = TestNumber()
myClassItertator = iter(myIterableClass)

for x in myClassItertator:
    print(x)