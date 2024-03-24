def main()-> None:
    try: # Good way to open files on python, closes the file after operation
        with open('text_file.txt', 'r') as text_file:
            print(text_file.read())
    
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
