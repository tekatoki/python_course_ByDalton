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

'''
def int_list(list):
    t = 0
    for i in list:
        list.insert(int(i), t)
        t += 1
    return list
'''

def assign_rol(int_array_iterable: list):
    '''
    This functions assigns a rol to the highest and lowest number
    of a given list of integres values. 
    '''
    int_array_iterable.sort(reverse=True)

    high_rol = int_array_iterable[0]
    low_rol = int_array_iterable[-1]

    return high_rol, low_rol 

if __name__ == '__main__':

    input = input('Introduce the age of each student, separate with a spacebar>')
    input = input.split()   
    list_student_ages = [int(i) for i in input]

    # A
    list_student_ages.sort(reverse = True)

    # Output
    print(f'The order of ages of the classmates are:{list_student_ages}')

    # B

    teacher_age, assistant_age = assign_rol(list_student_ages)

    # Output
    print(f'The teacher is {teacher_age} years old and the assistant is {assistant_age} years old')    
