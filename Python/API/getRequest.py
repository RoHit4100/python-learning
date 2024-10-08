import requests
res = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata')

data = res.json()
print(data)
print(type(data))

