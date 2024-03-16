def greet_python():
    print('Hi, Python!')

def greet_person(name: str, surname: str, formality: bool = False):
    if formality:
        print(f'Hello, dear Mr./Ms. {surname}')
    else:
        print(f'Hi, {name}')
