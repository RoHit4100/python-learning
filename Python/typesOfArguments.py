
def fun(name, age, *args):
    print(f'{name} {age}')
    print(args)
    
fun('rohit', 22, 2,2,3,4,4,23)
    
# by using * I can enforce to pass keyword parameters after *
def fun2(name, age, *, marks, salary):
    print(name)
    print(age)
    print(marks)
    print(salary)

fun2('rohit', 22, marks=99, salary='30k')

def fun1(**kvargs):
    print(type(kvargs))

fun1(name = 'rohit', city= 'thane')

