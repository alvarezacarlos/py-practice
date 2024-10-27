# A RegEx or regular expression, is a sequence of characters that forms a search pattern

# RegEx can be used to check if a string contains the specified search pattern.

#Built-in package called re, which can be used to work with regular expressions. 

import re

#check if a string starts with "The" and ends with "Spain"

string_data = "The rain in Spain"

res = re.search("^The.*Spain$", string_data)

# print(res)

if res:
    print('Yes!, we have a match!')
else:
    print('No Match Found!')

#RefEx functions : the re module offers a set of functions that allows us to serach a sting for a match: 

"""
    findall : Returns a list containing all matches
    search  : Returns a Match object if there is a match anywhere in the string
    split   : Returns a list where the string has been split at each match
    sub     : Replaces one or many matches with a string
"""
# read more : https://www.w3schools.com/python/python_regex.asp
