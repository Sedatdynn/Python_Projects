import requests
from bs4 import BeautifulSoup
import json
from dbConnect import connect


class Neu:
    def __init__(self,url):
        self.headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.newsUrl = url
        self.url = requests.get(self.newsUrl, headers=self.headers)
        self.news = self.url.content
        soup = BeautifulSoup(self.news, "html.parser")
        liste = soup.find("div", class_="posts-grid posts-grid-3 clearfix").find_all("article")
        self.db = connect()
        self.news_sum = False
        self.news_content = False
        self.news_date = False
        self.news_link = False
        self.current_doc = []
        self.datas = []

        self.my_json = {
            "neuNews": []
        }
        with open(r"D:\PycharmProjects\PYTHON\NeuNews.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for item in data["neuNews"]:
            try:
                self.current_doc.append(item["News Link"])
            except:
                pass
        self.haber(liste)

    def haber(self,data):
        try:
            count = 0
            for i in data:
                count +=1
                news_link = i.find('a')['href']
                if news_link in self.current_doc:
                    print("Veriler json dosyasında mevcut.")
                else:
                    self.news_link = i.find('a')['href']
                    self.news_sum = i.find("h2").text
                    self.news_content = i.find("div", class_="post-excerpt entry-summary").text.replace("daha fazla »", " ")
                    self.news_date = i.find("span", class_="post-date").text.strip("")

                    my_data = {
                        'News Title': self.news_sum,
                        'News Content': self.news_content,
                        'News Date': str(self.news_date),
                        'News Link': self.news_link,
                    }

                    self.datas.append(my_data)

        except:
            pass
        self.save(self.datas)

    def save(self,data):
        with open(r"D:\PycharmProjects\PYTHON\NeuNews.json", "r", encoding="utf-8") as file:
            js_file = json.load(file)

        for i in data:
            js_file["neuNews"].append(i)

        with open(r"D:\PycharmProjects\PYTHON\NeuNews.json", "w", encoding="utf-8") as file2:
            json.dump(js_file, file2, indent=2, ensure_ascii=False)

        print("Veriler json dosyasına eklendi.")
        self.save_to_db()

    def save_to_db(self):
        with open(r"D:\PycharmProjects\PYTHON\NeuNews.json", "r", encoding="utf-8") as file:
            to_db = json.load(file)

        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM neu_news")
        db_datas = []
        row = cursor.fetchall()
        for item in row:
            db_datas.append(item[1])

        for i in to_db["neuNews"]:
            if i["News Title"] in db_datas:
                print("bu veri veri tabanında mevcut.")
            else:
                insert_data = (
                    "INSERT INTO neu_news(NewsTitle, NewsContent, NewsDate, NewsLink)"
                    "VALUES (%s, %s, %s, %s)"
                )
                js_datas = (f'{i["News Title"]}', i['News Content'],  i['News Date'], i['News Link'])

                cursor.execute(insert_data, js_datas)

                self.db.commit()
        self.db.close()

url_list=["https://neu.edu.tr/category/haberler/","https://neu.edu.tr/category/kultursanat/","https://neu.edu.tr/category/duyurular/"]
for i in url_list:
    a = Neu(url=i)


