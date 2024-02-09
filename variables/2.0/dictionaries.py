'''
Dictionaries are extremelly useful when it comes to object orientared
programming. In this piece of code we'll see some useful ways to create 
dictionaries.

Dictionaries values can be seen via the debugger.
'''

# Using dict() function

dict_function_example = dict(name="John", surname="Adams", age=26)

# As lists are keys that cannot be hasheable, we have to use frozenset() to make it inmutable

list_inside_dict = {frozenset(["city", "street"]):'unknown'}
tuple_inside_dict = {("network_ip", "os"):'unknown'} # As tuples has a "__hash__" method, they're already inmutable

# Creating dictionaries with fromkeys()

dict_fromkeys_function = dict.fromkeys(['social_number','id'], 'Unknown') # If there's not second_parameter inside fromkeys() it will be None

