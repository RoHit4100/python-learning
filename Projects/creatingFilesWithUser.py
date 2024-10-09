# First get the file name
fileName = input('Enter the file name: ')

# Now get the content for that particular file
content = input("Enter content: ")

with open(fileName, 'w') as file:
    file.write(content)

# Now we will check if the user wants to write to the file again or not
while True:
    # Get the answer from the user if they want to append to the file or not
    answer = input('If you want to append type y, or else n or exit press x: ')
    
    if answer == 'y': 
        with open(fileName, 'a') as file:
            c = input('Enter the content: ')
            file.write(c)
    elif answer == 'n':
        # Ask if the user wants to read the file or not
        wantRead = input('Do you want to read the file? (y/n): ')
        if wantRead == 'y':
            with open(fileName, 'r') as file:
                print(file.read())
        break  # Exit the loop after reading the file
    elif answer == 'x':
        break  # Exit the loop if the user chooses 'x'
    else:
        print('Enter a valid key')
