'''
As well as lists and strings, dictionaries on python have their own methods to
change the value whithin the variable.

The changes of the values of the dict that methods do will be printed on command line wihout changing
the value of the original variable. 
'''

dict_example = {
    'name' : 'user_name',
    'age' : 23,
    'followers' : 23000,
    'hobbies': ['Coding', 'Chalisteincs', 'Surfing']
}

# key method

print(f'Key method output > {dict_example.keys()}')

# get method

print('Get method output > {}'.format(dict_example.get('followers')))

# clear method

print(f'Clear method output > {dict_example.clear()}')

# pop method in dict

print('Pop method output > {}'.format(dict_example.pop('age')))

# item method

print(f'Item method output > {dict_example.items()}')
