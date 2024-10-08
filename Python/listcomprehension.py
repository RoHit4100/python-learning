
# list comprehension is used as shorthand for, looping and adding to something in the list

# power 2
power2 = [num ** 2 for num in range(1, 11)]
print(power2)

# using if condition to filter some values in comprehension
f = [num for num in range(0, 20) if (num & 1) == 0]
print(f)


# in the matrix using comprehension
matrix = [[1,2,3], [4,5,6], [7,8,9]]

ans = [num for row in matrix for num in row]
print(ans)


# comprehension using functional programming
sum = 0
def add(x):
    global sum  # Declare sum as a global variable
    sum += x
    return sum

a = [add(num) for num in [1, 2, 3, 4, 5, 6]]
print(a)


