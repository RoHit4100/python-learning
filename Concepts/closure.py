

def closure():
    currentSum = 0
    def add(x):
        nonlocal currentSum
        # non local keyword will give the permission to inner function to modify the currentSum which present in 
        # the parent of add function, which will maintain its state, even after changed by add function
        currentSum += x
        return currentSum
    return add

# now store the closure to a variable
add = closure() 

ans = [add(num) for num in [1,2,3,4,5,6]]
print(ans)


def fun():
    x = 100
    def y(p): # we will pass the reference function in the return values, with it, its lexical environment is also passed
        print(x + p)
    return y

a = fun()
a(100)



# factory function
def outer(power):
    def inner(x):
        return x ** power
    return inner


powerOf2 = outer(2)
print(powerOf2)
powerOf5 = outer(5)

print(powerOf2(5))
print(powerOf5(2))