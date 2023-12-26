'''
In addition to strings, numbers and booleans. There're other type of data that can store a var.
These are:
    lists > Can store differents values with diferent type of data at the same time.
    tupla > Same as lists but these are CONST.
    set > Same as tuplas but there are no index available, and can not store duplicated values.
    dictionary > Same as a .json file
'''

example_list = [1, 'String', True, 3.3] # The index of these value start from 0

print(example_list[0]) # printed value > 1

example_tupla = (1, 'String', True, 3.3) # These values can not be changed throughout the code

example_set = {1, 'String', True, 3.3} # No index available, and the values can not be duplicated

example_dictionary = {    
    'name' : 'your_name', # 'key' : {value}
    'height' : 1.83,
    'Spanish nationality' : True
}

print(example_dictionary['height']) # printed value > 1.83
