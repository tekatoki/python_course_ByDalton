'''
Problem statement:

Create a function that returns the prime numbers
between 0 and the argument you insert on the terminal
'''


def search_divisors (number:int, only_primes_nums:bool=False):
    '''
    Searchs all the divisors of a number given.
    The flag only_primes_nums will show only the primes numbers 
    that are divisors of the number given.
    '''
    
    def find_divisors (number:int):
        '''
        Only finds the divisors, it does distinct between primes and normal
        numbers and return a list with all the divisors.
        '''
        
        divisors:list = []
        i: int = 1
        # Finds all the divisors
        for i in range(1, number):
            if 0 == number % i:
                if i in divisors: 
                    exit
                else:
                    divisors.append(i)
                    divisors.append(int(number / i))
            else:
                continue
            i += 1
        divisors.sort()
        return divisors
    

    if False == only_primes_nums:
        return find_divisors(number)
    
    if True == only_primes_nums:
        primes_nums:list = []

        for num in find_divisors(number):
            if [1, num] == find_divisors(num): # Looks if each number is a prime number 
                primes_nums.append(num)
            else:
                continue
        primes_nums.sort()
        return primes_nums

if __name__ == '__main__':
    print('====== Prime numbers divisible calculator ======')
    print('WARNING: This program only supports introduce a character that can be converted as a number, all decimals will be ignored')
    input_num = int(input('Introduce a number>'))

    print(f'Divisible primes numbers of {input_num} are: {search_divisors(input_num, only_primes_nums=True)}')
