'''
Variables are memory allocations for a value.
On python this value can be changed throughout the code and can change and you can change its type of data as well.
However, the practice mentioned previously it's a bad practice. You should avoid doing that.
'''  

a = 2
b = 3
c = a + b

print(c)

# There are different ways to set the name of a variable

helloWorld = 'Hello World!' # An example of camelCase {NOT STANDARD ON PYTHON}
hello_world = 'Hello World!' # An example of snake_case {STANDARD ON PYTHON}

# Now it'll be shown a property for string values, concatenation

concatenation_value = 'your_name'
welcome_message = f'Welcome, {concatenation_value}. How are you?' # {f} change all valuese to string in order to be compatible

print(welcome_message) # Welcome, your_name. How are you?
