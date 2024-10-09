
print("hello world")   

a = 10
print('a: ' + str(a))

for i in range(5):
    print(i)
    

mList = ['rohit', [1, 2, 23, 4], 66, 0.9]
mList.remove('rohit')
print(type(list))
for item in mList:
    if isinstance(item, list):
        for i in item:
            print("This is i "+ str(i))
    else:
        print(item)
