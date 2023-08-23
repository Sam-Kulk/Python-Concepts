# format() method is used for string formatting
# basically it will accept the agruments, puts them in the string & returns the new string
# it is also a string method

# Refer W3S's Python String/Format String & Python String Formatting for more details


txt = "My name is Samarth and I am {} of age"
print(txt.format(24))

txt = "My name is {} and I am {} of age"
print(txt.format('Samarth',24))

txt = "My name is {1} and I am {0} of age"
print(txt.format('Samarth',24))

txt = "My name is {0} and I am {0} of age"
print(txt.format('Samarth',24))

txt = "My name is {name} and I am {age} of age"
print(txt.format(name='Samarth',age=24))
