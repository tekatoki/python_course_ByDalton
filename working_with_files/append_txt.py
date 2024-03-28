def main()-> None:
    try:
        with open('append_file.txt', 'a') as file:
            for i in range(5): file.write(f'Line number {i+1} added\n')
            print('Operation finished succesfully')
    except Exception as error_read:
        print(error_read)
        exit

if __name__ == '__main__': 
    main()
