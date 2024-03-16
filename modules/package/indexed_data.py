def list_indexed_data():
    user_input:str = ''

    while user_input != '0' or user_input != '1':
        user_input = input('Do you want a tuple or a list [0 tuple / 1 list]> ')

        if '0' == user_input:
            return ('hi', 23.423, 53, 'world', False)
        elif '1' == user_input:
            return ['nothing', 'something', True, False]
