from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Star_wars"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso ao acessar a url")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string
    print(title)
    
    paragrafo_um = soup.find("p").text
    
    print(paragrafo_um)
    print("----------------------")
    
    paragrafos = soup.find_all("p")
    
    if len(paragrafos) > 1:
        print(paragrafos[1].text)
    else:
        print("Nao existe mais de 1 paragrafo")
        
    # <a href="url">clique aqui</a>
    
    links = soup.find_all("a", href=True)[:5]
    
    for link in links:
        print(link["href"])
    
    