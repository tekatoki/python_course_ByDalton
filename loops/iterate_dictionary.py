'''
Dictionaries are iterable by default, however if you want to iterate
both key and value you'll need to use items() mehtods.
In the following code there will be an example that will make easier to understand it.
'''

user_credentials = {
    'name' : 'John',
    'email' : 'johnny2000@hotmail.com',
    'password' : 'admin1234',
    'age': 24,
}

# Iterating only keys

for type_credential in user_credentials:
    print(type_credential)

# Iterating keys and values
# EXTRA: You can skip printing an iterable value by using continue function
    
for type_credential, data_credential in user_credentials.items():
    if 'password' == type_credential:
        continue 
    print(f"User's {type_credential} is {data_credential}")



