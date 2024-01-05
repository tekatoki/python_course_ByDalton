'''
There are several logical operators in order to set specific conditions in a if-else conditional.
The operators available on Python are the following:
    AND > All conditions must be true 
    OR > One condition have to be true
    NOT > Changes the boolean value 
'''
# Example of log in program to show a use of these logical operators

connected_internet = True
user_email = 'user_example@email.com'
user_password = 'Password example12345'

entered_email = input('Introduce your email >')
entered_password = input('Introduce your password>')

if not connected_internet:
    print('Not connected to the internet, could not connect to the server')
elif entered_email != user_email or entered_password != user_password:
    print('Email or password incorrect')
    exit
else:
    print('Valid credentials')

# Other way to do it, but less readable and efficient
'''
elif entered_email == user_email and entered_password == user_password:
    print('Valid credentials')
    exit
'''
