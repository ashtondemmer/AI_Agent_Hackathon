import requests

def fetch(category):
    category = "animals"
    #send request to api
    base_url = "https://api.publicapis.org/"
    endpoint = "random"
    params = {
        "category": category
    }
    response = requests.get(f'{base_url}{endpoint}', params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f'Error: {response.status_code}')

