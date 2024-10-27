"""
    The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")


#print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print('Variable x is not defined!')
except:
    print('Somthinf else went wrong!')


#else: you can use the else keyword to define a block of code to be executed if no erros were raised in the try block:
try:
    print('Hello there!')
except:
    print('Somthing went wrong!')
else:
    print('Nothing went wrong!')

#finally: if you specify the finally block will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print('Something went wrong!')
finally:
    print('The try except is done!')


#this is very useful to close objects and clear up resources:
try:
    f = open('demofile.txt')
    try:
        f.write('Dummy Data')
    except:
        print('Something went wrong when writing to the file!')
    finally:
        f.close()
except:
    print('Something went wrong when opening the file')


# raise : we can choose to throw an exception if a condition occurs.
#In this case we will raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
    # raise Exception('Sorry, no numbers below zero!')
    pass

#We can choose what type of error to raise based on the scenario
#Lets raise a TypeError if the var_name is not integer
var_name = 'hello'
if not type(var_name) is int:
    raise TypeError('Only Integers are allowed!')

