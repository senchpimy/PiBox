from bs4 import BeautifulSoup as bs
import requests
import re
import json

class youtube:
    def __init__(self,url):
     #url = "https://www.youtube.com/@ThePrimeTimeagen/about"
        self.soup = bs(requests.get(url, cookies = {'CONTENT':'YES+1'}).text,"html.parser")
        self.data = re.search(r"var ytInitialData = ((.*));", self.soup.prettify()).group(1)

    def get_channel_about(self):
        """"https://www.youtube.com/XXXXXXX/about"""
        json_data = json.loads(self.data)
        # 'channelId','title', 'avatar''thumbnails'2'url' 
        channelId = json_data['header']['c4TabbedHeaderRenderer']['channelId']
        title = json_data['header']['c4TabbedHeaderRenderer']['title']
        avatar = json_data['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][2]['url']
        print(channelId, title, avatar)

    def get_channel_main(self):
        """"https://www.youtube.com/XXXXXXX/videos"""
        json_data = json.loads(self.data)
        data = json_data['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents']
        for i in data:
            try:
                titulo = i['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                thumbnail = i['richItemRenderer']['content']['videoRenderer']['thumbnail']['thumbnails'][3]['url']
                duracion = i['richItemRenderer']['content']['videoRenderer']['lengthText']['simpleText']
                enlace = i['richItemRenderer']['content']['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                print(titulo, thumbnail, duracion,enlace)
            except:
                continue

    def search(self):
        json_data =json.loads(self.data)
        data = json_data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
        #print(json.dumps(data, indent=2))
        for i in data:
            try:
                print(i['videoRenderer']['title']['runs'][0]['text']) #Titulo
                print(i['videoRenderer']['thumbnail']['thumbnails'][0]['url']) #thumbnail
                duracion = i['richItemRenderer']['content']['videoRenderer']['lengthText']['simpleText']
                enlace = i['richItemRenderer']['content']['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                print(duracion,enlace)
            except:
                print("LALALL")



yt = youtube("https://www.youtube.com/results?search_query=pissy+pamper")
yt.search()
