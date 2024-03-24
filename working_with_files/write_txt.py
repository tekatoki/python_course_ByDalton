def write_file(message_in:list[str])-> None:
    try:
        with open('writing_file.txt', 'w') as file:
            file.writelines(message_in)

    except Exception as error_file: # As write mode creates a new file, it's impossible that will be necessary to catch an exception 
        print(error_file)
        exit() 


def main()-> None:
    write_file(input('Write what you want to write in the file: \n'))

if __name__ == '__main__':
    main()

