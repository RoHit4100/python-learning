
n = 1234567

while n > 0:
    rem = n % 10
    print(f"{int(rem)}", end='')
    n = int(n / 10)

