name = 'Carlos' #declare a variable which is global and can be accessed from the funcion myFn becaus is in a highier scope
def myFn():  # myFn
    
    global name #we need to access the name variable first with the global variable to tell python that we are interacting with the global variable.

    print(name) #access the global variable name. We can access the global variable name but if we try to change its value python will understand that we are trying to create a local variable called with the same name. it it does not know if we are trying to print the name local variable or the global one.
    
    name = 'Mark'   #we can now change the name variable value and python will understand that we are trying to modify the global variable. 
    
myFn()
print(name)


def myFn_1():
    global age #Global variable declared in a function scope
    age = 55 #Assign a value to the global variale. 
    #for this variable age to be access from outside we need to execute/call this function first for this variable to declared and initialized
    
myFn_1() # Call of the function which creates the variable age and initializes it, so we can access it below.
print(age) #Access the variable from outside the function scope
