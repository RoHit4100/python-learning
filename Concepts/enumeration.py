
li = [1,3,4,7,5,2]

# with the help of enumeration, we can get the indexes of lists
for index, value in enumerate(li):
    if(index & 1) == 1: 
        print(f'{index}: {value}')