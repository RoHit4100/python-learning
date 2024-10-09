
def myGenerator(): 
    for num in range(1, 13):
        yield num ** num
    
exp = myGenerator()
print(exp)

for bigNum in myGenerator():
    print(bigNum)


li = list(myGenerator())
print(li)

