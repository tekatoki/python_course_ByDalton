import div_op as div

if __name__ == '__main__':
    num_input = int(input('Introduce a number>'))
    prime_ask_input = input('Do you want to only show prime numbers [y/n]>')
    
    if 'y' == prime_ask_input:
        print(f'All the prime divisors of {num_input} are {div.search_divisors(num_input, only_primes_nums=True)}')
    elif 'n' == prime_ask_input:
        print(f'All the prime divisors of {num_input} are {div.search_divisors(num_input)}')
    else:
        print('Next time introduce a valid answer.')
    
    print('Exiting program')
