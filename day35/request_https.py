import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso!")
    data = response.json()
    
    print("Essa é a piada do Chuck Norris: ")
    print(data['value'])
else: 
    print("Erro de chamar a API do Chuck Norris.")
    
