'''
In order to change the values inside a list, there are several methods that can change the a value inside these.
In this python file we'll see some examples

You can see the changes of the values of the list throughout the code using the debugger by setting a breakpoint in all 
the methods examples.
'''

# list function

list_example = list(['hi', 'hello', 4.3, 8, False]) 

# len function

len_function = len(list_example)

# append method

list_example.append(True) 

# insert method

list_example.insert(0, 'python') 

# extend method

list_example.extend(['Cyberpunk', 2077]) 

# pop method

list_example.pop(0) 

# remove method

list_example.remove(False)

print('This print is only used to set a breakpoint before')

# clear method

list_example.clear()

# sort method

list_only_num = [1, 4, 4.2, 2783, 2099, 2024]
list_only_num.sort()

# sort method but inverted

list_only_num.sort(reverse=True)

# reverse method

list_example.reverse() 


print('This print is only used to set a breakpoint in the line before')
