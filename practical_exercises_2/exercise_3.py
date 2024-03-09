'''
Problem statement:

Create a function that prints the Fibonacci's succesion until a number given
'''

def fibonacci_succesion (limit:int):
    a, b = 0, 1
    fibonacci_nums: list = [0] # It starts by the first value of a
    for i in range(limit):
        fibonacci_nums.append(b)
        a, b = b, a+b
    
    print(fibonacci_nums)
    '''
    print(a)
    print(b)
    for i in range(limit):
        a += b
        print(a)
        b += a
        print(b)
    '''
if __name__ == "__main__":
    limit_input:int = int(input('Introduce a limit for the fibonacci succesion>'))
    fibonacci_succesion(limit_input)
