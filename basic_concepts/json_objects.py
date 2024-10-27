# JSON is a syntax for storing and exchanging data.  JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.

#import the jaon built-in package
import json

# json.loads() : parse from json to python's dictionary. if you have a string, you can parse it by using the json.loads() method. The result will be a Python dictionary.
#json string data
json_string_data = '{ "name":"Jhon", "age":45, "city":"Panama" }'  

#parse the data in a json format with string type to a python dictionary
dictionary = json.loads(json_string_data)

print(dictionary)
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['city'])


#json.dumps() : a python object can be cconverted to json by using the json.dumps() method
json_result = json.dumps(dictionary)
print(json_result)


"""
You can convert Python objects of the following types, into JSON strings:
    dict
    list
    tuple
    string
    int
    float
    True
    False
    None
    
    Examples: 
        json_result_from_dictionaty = json.dumps({"name": "John", "age": 30})
        json_result_from_list = json.dumps(["apple", "bananas"])
        json_result_from_tuple = json.dumps(("apple", "bananas"))
        json_result_from_string = json.dumps("hello")
        json_result_from_integer = json.dumps(42)
        json_result_from_float = json.dumps(31.76)
        json_result_from_boolean = json.dumps(True)
        json_result_from_boolean = json.dumps(False)
        json_result_from_None = json.dumps(None)
"""

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

    Python	            JSON
    dict	    ->      Object
    list	    ->      Array
    tuple	    ->      Array
    str	        ->      String
    int	        ->      Number
    float	    ->      Number
    True	    ->      true
    False	    ->      false
    None	    ->      null
"""


#use the ident parameter to ident a json objet when printing it
api_response = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

res = json.dumps(api_response, indent=4)
print(res)


#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

res_1 = json.dumps(api_response, indent=4, separators=(". ", " = "))
print(res_1)


#order the result: The json.dumps() method has parameters to order the keys in the result
#Use the sort_keys parameter to specify if the result should be sorted or not:
res_2 = json.dumps(api_response, indent=4, sort_keys=True)
print(res_2)


