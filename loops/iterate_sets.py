'''
In order to iterate sets using a for loop you have to use the 
enumerate() function to convert the set into a tuple so it can be iterable.
In other words, as it has a key and a value can be iterate, being the key, the index.
'''

num_set = {23, 52, 1, 3, 9.1}

for i,num in enumerate(num_set):
    print(num)
