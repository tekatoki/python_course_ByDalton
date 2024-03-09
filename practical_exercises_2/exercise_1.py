'''
Problem statement: 

The teacher didn't come today. So in order to still be able to do class
one student will have the rol of the teacher and another one will be
the his assistant.

A) Ask the age of the classmates that came to class and sort the de ages
from oldest to youngest.

B) The oldest is the teacher and the youngest is the assistant. How old
are both the teacher and assistant?
'''


def a_part (list_students : list):
    list_students.sort(key = lambda x:x[0], reverse = True) # Only x is int value of each object tuple

    print('The order of the ages of classmates are:')
    
    for i in list_students: # Output for the sorted algorithm
        print(f'- {i[1]} is {i[0]} years old')  

def combine_data (iterable_1 : list, iterable_2 : list):
    t = 0
    list_return = []
    for i in iterable_1:
        list_return.append((int(iterable_1[t]), iterable_2[t]))
        t += 1
    return list_return

def assign_rol(tuple_array_iterable: list):
    '''
    This functions assigns a rol to the highest and lowest number
    of a given list of integres values.
    The function expects that the iterable objects inside the array 
    are tuples. 
    '''

    tuple_array_iterable.sort(key = lambda x:x[0], reverse=True)

    high_rol = tuple_array_iterable[0]
    low_rol = tuple_array_iterable[-1]

    return high_rol, low_rol 


if __name__ == '__main__':

    input_ages = input('Introduce the age of each student, separate with a spacebar>')
    input_ages = input_ages.split()
    
    input_names = input('Introduce the names with the same order>')
    input_names = input_names.split()

    list_students = combine_data(input_ages, input_names)

    print('\n')
    
    # A
    a_part(list_students)

    # B
    teacher_info, assistant_info = assign_rol(list_students)
    print(f'\nThe teacher is {teacher_info[1]} and the assistant is {assistant_info[1]}\n') # Output_b  
