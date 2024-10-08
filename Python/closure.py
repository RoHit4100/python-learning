

def closure():
    currentSum = 0
    def add(x):
        nonlocal currentSum # non local keyword will give the permission to inner function to modify the currentSum which present in 
        # the parent of add function, which will maintain its state, even after changed by add function
        currentSum += x
        return currentSum
    return add

# now store the closure to a variable
add = closure()

ans = [add(num) for num in [1,2,3,4,5,6]]
print(ans)