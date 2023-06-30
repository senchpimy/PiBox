from bs4 import BeautifulSoup as bs
import requests

class animeflv:
    def __init__(self, url):
        data = requests.get(url, cookies = {'CONTENT':'YES+1'})
        self.data = bs(data.text, "html.parser")
    def get_video(self):
        #a = animeflv("https://animeflv.vc/my-home-hero-12")
        #Opcion 3, o dominio streamtape, div.load_video>iframe*src
        #Stramtape video#mainvideo*src directo a mpv
        print()

    def get_channel_main(self):
        titulo = self.data.body.h2.text
        desc = self.data.find("div", {"class":"Description"}).text
        print(titulo)
        print(desc)

a = animeflv("https://animeflv.vc/anime/my-home-hero")
a.get_channel_main()
