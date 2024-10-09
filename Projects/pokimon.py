# import requests to make HTTP requests
import requests

# get the Pokemon name from the user
name = input('Enter the name of the Pokemon: ')
name = name.lower()
# make a GET request to the PokeAPI for the specified Pokemon
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')

# check if the request was successful
if res.status_code == 200:
    # parse the JSON response data
    data = res.json()

    # loop through the abilities and print each ability name
    for ability in data['abilities']:
        print(ability['ability']['name'])  
        # in this ability we have the name and url for that ability
        url = ability['ability']['url']
        # print(url)
        r = requests.get(url)
        d = r.json()
        # print(d)
        for effect in d['effect_entries']:
            print(effect['effect'])
else:
    # if the Pokemon name is invalid or not found
    print('Enter valid Pokemon name')
