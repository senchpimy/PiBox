from bs4 import BeautifulSoup as bs
import requests
import re
import json

     #url = "https://www.youtube.com/@ThePrimeTimeagen/about"
def name():
    name="YouTube"
    return name
def svg():
    svg= '<svg xmlns="http://www.w3.org/2000/svg" height="100%" width="100%" viewBox="50 0 150 150"><path d="M229.763 25.817c-2.699-10.162-10.65-18.165-20.748-20.881C190.716 0 117.333 0 117.333 0S43.951 0 25.651 4.936C15.553 7.652 7.6 15.655 4.903 25.817 0 44.236 0 82.667 0 82.667s0 38.429 4.903 56.85C7.6 149.68 15.553 157.681 25.65 160.4c18.3 4.934 91.682 4.934 91.682 4.934s73.383 0 91.682-4.934c10.098-2.718 18.049-10.72 20.748-20.882 4.904-18.421 4.904-56.85 4.904-56.85s0-38.431-4.904-56.85" fill="red"/><path d="M93.333 117.559l61.333-34.89-61.333-34.894z" fill="#fff"/></svg>'
    return svg

def get_channel_about(url):
    """"https://www.youtube.com/XXXXXXX/about"""
    soup = bs(requests.get(url, cookies = {'CONTENT':'YES+1'}).text,"html.parser")
    data = re.search(r"var ytInitialData = ((.*));", soup.prettify()).group(1)
    json_data = json.loads(data)
    # 'channelId','title', 'avatar''thumbnails'2'url' 
    channelId = json_data['header']['c4TabbedHeaderRenderer']['channelId']
    title = json_data['header']['c4TabbedHeaderRenderer']['title']
    avatar = json_data['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][2]['url']
    print(channelId, title, avatar)

def get_channel_main(url):
    """"https://www.youtube.com/XXXXXXX/videos"""
    soup = bs(requests.get(url, cookies = {'CONTENT':'YES+1'}).text,"html.parser")
    data = re.search(r"var ytInitialData = ((.*));", soup.prettify()).group(1)
    json_data = json.loads(data)
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

def search():
    soup = bs(requests.get(url, cookies = {'CONTENT':'YES+1'}).text,"html.parser")
    data = re.search(r"var ytInitialData = ((.*));", soup.prettify()).group(1)
    json_data =json.loads(data)
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



#yt = youtube("https://www.youtube.com/results?search_query=pissy+pamper")
#yt.search()
