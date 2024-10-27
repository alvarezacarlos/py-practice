# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His last age is " + str(kid["age"]))

my_function(fname = "Tobias", lname = "Jhon", age=45)