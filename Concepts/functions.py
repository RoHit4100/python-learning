
# def fun():
#     print(f'name {name}')
    
# name = 'rohit'
# print(fun)


def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(10))


def fun1(name):
    print(f'name is {name}')
    def fun2():
        print(f'inside nested function {name}')
    fun2()
    
    

def function(name, *args):
    print(type(name))
    print(type(args))
    print(args)
    
function('rohit', 1,2,3,4,5,6,7,8,'dakshata')
# def pow(a, b):
#     return a ** b

# print(pow(2,3))