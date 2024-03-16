import div_op as div
import package.greet 
import package.indexed_data

if __name__ == '__main__':
    name_input:str = input('Introduce your name>')
    surname_input:str = input('Introduce your surname>')

    num_input:int = int(input('Introduce a number>'))
    prime_ask_input:str = input('Do you want to only show prime numbers [y/n]>')
    
    if 'y' == prime_ask_input:
        print(f'All the prime divisors of {num_input} are {div.search_divisors(num_input, only_primes_nums=True)}')
    elif 'n' == prime_ask_input:
        print(f'All the prime divisors of {num_input} are {div.search_divisors(num_input)}')
    else:
        print('Next time introduce a valid answer.')
    
    print(package.greet.greet_person(name_input, surname_input))
    print(package.indexed_data.list_indexed_data())
    
    print('Exiting program')
