'''
In this piece of code we'll see examples of built-in functions that are available in python out of the box.
These functions are isolated piece of code that runs whenever we call them.
'''

num = {4,9,3.141592654,265}

print(f'The maximum number value in the set is {max(num)} and the minimum is {min(num)}')

print(f'The pi number with two decimals of approximation is {round(min(num),2)}')


''' 
bool() function returns False --> 0, empty array, False, none
                returns True --> int/float != 0, True, string
'''
print(bool(0))
print(bool('Hello World!'))

# Same as bool() but with all the elements of and iterable var

print(all([12, 3, 2, "hello", "World"]))

