'''
Lambda functions are declared in a single line of code and can't be called with a name throughout the code.
These are very useful in order to not make simple operations that are pretty simple and easy to understand.
'''

if __name__ == '__main__':
    nums = {2,3,45,3.2,34,4,6,7}

    even_nums = filter(lambda num: num % 2 == 0, nums)
    odd_nums = filter(lambda num: num % 3 == 0, nums)

    print(f'In the set... \n- The even numbers are:{list(even_nums)} \n- The odd numbers are:{list(odd_nums)}')
