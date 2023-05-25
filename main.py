"""import urllib.request
opener = urllib.request.build_opener()
response = opener.open ("https://httpbin.org/")
print(response.read())
print("riznica")"""
import requests
response = requests.get("https://httpbin.org/")
"""print(response.text)
response_parse = response.text.split("<span>")
for elem in response_parse:
    if elem.startswith("$"):
        print(elem)"""
from bs4 import BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features= "html.parser")
    soup_list = soup.findAll('a', {'href': "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(res.text)