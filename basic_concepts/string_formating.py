# The format() method allows you to format selected parts of string.
# it works adding placeholders {} (curly brackets) in the text, and run the values through the format() method.

price = 49
txt = 'The price is: {} dollars'

complete_txt = txt.format(price)

print(complete_txt)

#read more at: https://www.w3schools.com/python/python_string_formatting.asp