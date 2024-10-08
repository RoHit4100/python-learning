
# without dictionary comprehension

names = [('name', 'rohit'), ('friend', 'dakshata')]

di = {}

for key, value in names:
    di[key] = value

print(di)


# with dictionary comprehension
d = {key:value for key, value in names}
print(d)


dd = dict(names)
print(dd)