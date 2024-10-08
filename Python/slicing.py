
# slicing with the help of the indexing

li = [1,2,3,3,4,5,6,7]

print(li[0::]) # from 0 to end
print(li[0: 5]) # from 0 to 5, where 5 is exclusive
print(li[-1]) # negative index means index from the end of the array

print(li[-3::])   


str = 'My name is rohit'
for i in str:
    if i == ' ':
        continue
    print(i)
    
    
print(li[::-1])