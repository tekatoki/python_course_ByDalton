'''
In order to iterate values of a list or tuple it is fundamental
to understand for loops.
In this code there will be some examples of how to create these kind
of loops on python.
'''

animals = ['fish', 'dog', 'cocodrile', 'cat']
numbers = [1.34, 3.141592, 24, 3]

'''
for animal in animals:
    print(animal)

for num in numbers:
    print(num * 2)
'''

# This for loop do the same that the commented one despite that it prints alternatively both values lists
for animal, num in zip(animals, numbers):
    print(animal)
    print(num * 2)

# Using range to imprint a series of numbers

print('Printing numbers from 0 to 5')
for num in range(6):
    print(num)
else:
    print('Loop for range(6) finished')

'''
This is no an optimal way to iterate a list

for animal in range(len(animal)):
    print(animal)

'''

# Optimal way to iterate a list
'''
for num in enumerate(numbers): # Enumerate creates a tuple
    key_numbers, value_numbers = num
    print(f'Index > {key_numbers}, value > {value_numbers}')
'''
# More elegant compared to the commented code

for i,num in enumerate(numbers):
    print(f'Index > {i}, value > {num}')

# A string is also a list, so it can be iterated

english_idiom = 'Kill two birds with the same stone'

for letter in english_idiom:
    if ' ' == letter:
        continue
    print(letter)

# One-line for loop

print([x*2 for x in numbers])
