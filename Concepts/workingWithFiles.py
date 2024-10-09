
# with keyword helps to open the files, with pythonic error handling, without using with keyboard may lead to error sum code
# 'with' keyword will make sure that file is closed after execution of that particular box

# without using with keyword
file = open('readme.txt', 'r') # this will return the reference object of that particular file
# print(file)
try:
    data = file.read()
    print(data)
except FileNotFoundError:
    print('file not found')
finally:
    file.close() # this will ensure that file is closed at any cost

# r will help to read the file
with open('readme.txt', 'r') as file: 
    content = file.read()

print(content)


# for creating the file
# if write is already present in the current path, then 'w' will override all the content present in that partcular file
with open('demo.txt', 'w') as file:
    file.write('This file is created with the help of python')


# if want to append the content then use the 'a' flag


# reading the file line by line
with open('fake_emails.txt', 'r') as emails:
    # now read file with the help of readFiles function
    # print(emails.readlines()) this will give u the array of the lines
    allEmails = emails.readlines()
    # as this is array we can traverse and perform logic over this file
    for mail in allEmails:
        if 'sophia.brown@placeholdermail.com' in mail:
            print("found")
            break
        