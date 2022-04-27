import requests


status = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

json_data = status.json()