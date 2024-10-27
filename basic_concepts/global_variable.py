user = 'Carlos'

def test():
    
    #creating a global varibal inside the function
    global x
    x = 5
    
    # Modify a global variable's value
    global user
    user = 'Jhon'
    

print(user)
    
test()

print(x)

print(user)