from bs4 import BeautifulSoup as bs
import requests

url = "https://www3.animeflv.net/"
data = requests.get(url)
print(data.text)
