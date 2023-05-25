import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.example.com/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    for script in soup.find_all(["style", "script"]):
        script.extract()#virizae HTML prikoli
    text = ' '.join(soup.stripped_strings)#vidrizae zayve HTML prikoly
    words = len(text.split())
    print(words)