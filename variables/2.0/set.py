'''
Sets are a very useful type of date when it comes to verify
that some data is inside another set. Even though right now
it's hard to explain more specific utilities, it will me be handful in
the future. 
'''

# Using function set() to create a set

set_example = set([1,2,3])

# In order to put a set inside another set you need to make the set inside inmutable

set_inmutable = frozenset(['inmutable', 'data']) # As set is not inmutable by default, is unhasheable
set_with_set = {'mutable', 2.4, set_inmutable}

# Set's theory utilities

set_a = {2,3,5,3.3}
set_b = {3,4}
set_c = {2,3,3.3}

# Testing the properties of the set declared

print(f'Set C is a subset of Set A > {set_c <= set_a} \n A value of set B is not inside set A > {set_b.isdisjoint(set_a)}')

