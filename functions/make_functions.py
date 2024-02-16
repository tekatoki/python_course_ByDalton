'''
In order to create functions on python (functions are isolated piece of code that can be called anywhere throughout the code)
you will have to use def(), the variables that you create inside the parentesis are "arguments" and are temporary variables
that can be called only inside the function.
Now we'll see an example of how to use it.
'''

'''
def arg_function (*args): # arguments with * are unlimited stored data
    for i in args:
        print(i)

def welcome_user (name = 'Anonymus'): # This is a keyword arguments, sets a value by default
    print('Hello, {name}. How are you?')
    # welcome_user() --> 'Hello, Anonymus, How are you?'
    # welcome_user(name = 'John') --> 'Hello, John. How are you?'
    
'''
def divider_line ():
    print('-' * 10)

def sign_up (): # By the other hand this returns a dict
    '''
    Creates a new user with its credentials.
    '''
    print("Now you're signing up a new account, introduce your credentials")
    divider_line()

    user_email = input('Email>')
    user_password = input ('Password>')
    retry_password = input('Introduce your password again>')
    
    while retry_password != user_password:
        print("Passwords doesn't match")
        retry_password = input('Intruduce your password again>')
    
    divider_line()

    return {'email': user_email, 'password': user_password}



def credentials (): # This function returns a tuple. credentials() --> (str{email_in}, str{password_in},)
    '''
    Documentation of the function credentials()

    Ask the user for its email and password and return it into a tuple --> email[0], password[1]
    Recommend to unpack tuple. 
    '''

    email_in = input('Introduce your email>')
    password_in = input('Introduce your password>')
    return email_in, password_in

# Function that doesn't return any value
def authentication (email, password):
    '''
    Authenticates email and password of a registered user.
    Authentication process won't stop unless the the credentials are valid.
    '''

    print("Now you're logging in, introduce your credentials.")
    divider_line()

    email_in, password_in = credentials()
    
    while email != email_in or password != password_in:
        print('Email or password incorrect, try again.')
        email_in, password_in = credentials()
    
    print('Credentials correct, loggin in...')
        
if __name__ == '__main__':
    user_credentials = sign_up()
    authentication(user_credentials['email'], user_credentials['password'])
