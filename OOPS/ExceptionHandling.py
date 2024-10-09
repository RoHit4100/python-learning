
# try: 
#     div = 100 / 0
# except Exception: 
#     print(Exception.__cause__)
    

# try:
#     num = input("Enter your roll number? ")
#     num = int(num)
# except Exception: 
#     num = 'unknown'

# print(num)


# using only specific exception

num1 = input('Enter first number: ')
try:
    num1 = int(num1)
    num2 = input('Enter second number: ')
    num2 = int(num2)
    div = num1 / num2
    print(div)
except ValueError as e: # this shows the specific value error, which will be catch by the error handling of the python
    print(e)
except ZeroDivisionError as e: # this will indentify the zero division execption
    print(e)
except Exception as e: # this will identify all the exceptions
    print(type(e))
