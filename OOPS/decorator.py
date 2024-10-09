def myDecorator(func):
    print('This is inside myDecorator')
    def inner():
        print('This is inside innner')
        func()
        print('After calling the function')
    return inner


@myDecorator
def myFunc():
    print('This is present inside myFunction')

# myFunc = myDecorator(myFunc) this will also work the same, but using decorator will be syntactic sugar
myFunc()