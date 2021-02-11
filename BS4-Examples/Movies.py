from bs4 import  BeautifulSoup
import requests



def veri_cek():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    site = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512/item/bonnie-clyde-hollywoods-100-favorite-818478")
    team = site.content
    soup = BeautifulSoup(team, "html.parser")

    alls = soup.find("ol",{"class": "list--ordered__items"}).find_all("li")
    count = 101

    for i in alls:
        count-=1
        title = i.h1.text
        director = i.find("div",class_ = "list-item__body js-fitvids-content").find("p").text
        cast = i.find("div",class_ = "list-item__body js-fitvids-content").find_all("p")[1].text
        word = i.find("div",class_ = "list-item__body js-fitvids-content").find_all("p")[3].text
        with open("D:\PycharmProjects\PYTHON\movies.txt", "a", encoding="utf-8") as file:
            file.write(str(count)+"-Movie Name:"+ title.replace("&nbsp", "")+" "+director.replace("&nbsp", " ")+" "+cast.replace("&nbsp", " ")+" "+ word.replace("&nbsp", " ")+" "+"\n")


veri_cek()