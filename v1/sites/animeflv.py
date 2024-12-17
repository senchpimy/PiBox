
def name():
    name="AnimeFLV"
    return name

def svg():
    svg= 'animeflv'
    return svg

def get_video(url):
    from bs4 import BeautifulSoup as bs
    import requests
    data = requests.get(url, cookies = {'CONTENT':'YES+1'})
    data = bs(data.text, "html.parser")
    #a = animeflv("https://animeflv.vc/my-home-hero-12")
    #Opcion 3, o dominio streamtape, div.load_video>iframe*src
    #Stramtape video#mainvideo*src directo a mpv
    print()

def get_channel_main(url):
    from bs4 import BeautifulSoup as bs
    import requests
    data = requests.get(url, cookies = {'CONTENT':'YES+1'})
    data = bs(data.text, "html.parser")
    titulo = data.body.h2.text
    desc = data.find("div", {"class":"Description"}).text
    print(titulo)
    print(desc)

    #a = animeflv("https://animeflv.vc/anime/my-home-hero")
    #a.get_channel_main()
