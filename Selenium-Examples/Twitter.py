from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twitterUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import  json


class Twitter:
    def __init__(self,username,password,hashtag):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Desktop\chromedriver.exe")
        self.username = username
        self.password = password
        self.hashtag = hashtag

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        signButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(5)
        self.browser.maximize_window()
        time.sleep(5)
        self.Search(self.hashtag)

    def Search(self,hashtag):
        searchInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        time.sleep(5)
        searchInput.send_keys(hashtag)
        time.sleep(5)
        searchInput.send_keys(Keys.ENTER)

        time.sleep(5)

        click_lastly = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a')))
        click_lastly.click()

        i = 500
        while i <= 2000:
            self.browser.execute_script(f"window.scrollTo(0, {i})")

            time.sleep(2)
            i += 500

        time.sleep(3)
        page_source = self.browser.page_source
        data = BeautifulSoup(page_source,"html.parser")

        profile_hrefs = data.find_all('a', class_='css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1loqt21 r-1adg3ll r-ahm1il r-1ny4l3l r-1udh08x r-o7ynqc r-6416eg r-13qz1uu')

        profile_nickname = data.find_all('div',class_='css-901oao css-bfa6kz r-9ilb82 r-18u37iz r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0')[1:]

        profile_name = data.find_all('div',class_='css-901oao css-bfa6kz r-1fmj7o5 r-1qd0xha r-a023e6 r-b88u0q r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0')[1:]

        profile_images = data.find_all('div',class_='css-1dbjc4n r-sdzlij r-1p0dtai r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-zchlnj r-ipm5af r-417010')[1:]

        tweet_ptime = data.find_all('a',class_='css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0')[1:]

        tweet_statics = data.find_all('div', class_='css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks r-1mdbhws')[1:]

        tweet_texts = data.find_all('div',class_='css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')[1:]
        my_json = {"postlar": []}

        for x in range(0, len(tweet_ptime)):
            hrefs = "https://www.twitter.com" + profile_hrefs[x]['href']

            nick_names = profile_nickname[x].find('span').text.strip()

            p_images = profile_images[x].find('img')['src']

            names = profile_name[x].find('span').text.strip()

            post_time = tweet_ptime[x].find('time').text.strip()

            post_texts = tweet_texts[x].text

            like_com_rt = tweet_statics[x]['aria-label']
            tw_stats = [int(s) for s in like_com_rt.split() if s.isdigit()]

            if not tw_stats:
                tw_stats.append(0)
                tw_stats.append(0)
                tw_stats.append(0)

            elif len(tw_stats) == 1:
                tw_stats.append(0)
                tw_stats.append(0)

            elif len(tw_stats) == 2:
                tw_stats.append(0)

            data = {"ProfileHref": hrefs,
                    "ProfileNick": nick_names,
                    "ProfileImage": p_images,
                    "ProfileNames": names,
                    "PostTime": post_time,
                    "PostTexts": " ".join(post_texts.split()),
                    "PostStats": tw_stats}
            my_json["postlar"].append(data)

        with open("tweets.json", "w", encoding="utf-8") as file:
            json.dump(my_json, file, ensure_ascii=False, indent=4)


twitter = Twitter(username,password,"Galatasaray")
twitter.signIn()
