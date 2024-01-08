'''
In order to change the value of a string (that works as an object or array), we use methods.
In this example of code we'll show some examples of these methods and how they work.

Structure of methods > {value}.{method}()

The values of the variables can be seen via the debbuger. 

The comment next to the variable will show the value as well so everyone seeing the code on
gihub can see the value without the necessity of installing the code in their computer.
'''

var_string_example = "Hello World!"

# dir function

dir_function = dir(var_string_example) # var_string_example's attributes

# .upper method
upper_case = var_string_example.upper() # HELLO WORLD!

# .lower method
lower_case = var_string_example.lower() # hello world!

# .capitalize method
capitalize_method = var_string_example.capitalize() # Hello world!

# .find method 
find_method = var_string_example.find('H') # 0

'''
The find method indexes a string to find the value you has given as a parameter.
It indexes all the letters of the string.
If the {parameter_value} given to the method is not in the {value} then, it will return -1
'''

# .index method

index_method = var_string_example.index('3') # exception, if {parameter_value} not found, gives exception

# .isnumeric method

isnumeric_method = var_string_example.isnumeric() # false
# .isalpha method 

isalpha_method = var_string_example.isalnum() # false // alpha numeric numbers are only letters and decimal numbers
 
# .count method

count_method = var_string_example.count('l') # 3

# len function

len_function = len(var_string_example) # 12

# .startswith method

startswith_method = var_string_example.startswith('H') # true

# .endswith method

endswith_method = var_string_example.endswith('!') # true

# .replace method

replace_method = var_string_example.replace('World', 'Python') # Hello Python!

# .split method

split_method = var_string_example.split(' ') # ['Hello', 'World!']
