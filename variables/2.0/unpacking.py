# The technique of unpacking consists of assigning a value to a variable that is available in a tuple or list

credentials_person = ['Johnson', 'Adams', 23, 'Netherlands']

credentials_person_tuple = ('Jordan', 'Patcher', 19, 'United States from America')

name_user_1, surname_user_1, age_user_1, country_born_user_1 = credentials_person

name_user_2, surname_user_2, age_user_2, country_born_user_2 = credentials_person_tuple

print(f'The user: {name_user_1} is from {country_born_user_1} and is {age_user_1} years old.')
print(f'The user: {name_user_2} is from {country_born_user_2} and is {age_user_2} years old.')
