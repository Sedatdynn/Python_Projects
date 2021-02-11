from instagramUserinfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Desktop\chromedriver.exe")
        self.username = username
        self.password = password

    def sıgnIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        self.browser.maximize_window()
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def follow(self,OtherUser):
        UserProfile = self.browser.get(f"https://www.instagram.com/{OtherUser}/")
        follow = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
        follow.click()

    def unfollow(self,userName):
        UserProfile = self.browser.get(f"https://www.instagram.com/{userName}/")
        time.sleep(2)
        unf = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button/div')
        unf.click()
        time.sleep(2)
        unfs = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
        unfs.click()

    def getFollowers(self):
        self.browser.get(f'https://www.instagram.com/{self.username}')
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]').click()
        time.sleep(3)
        dialog = self.browser.find_element_by_css_selector("div[role =dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"Followers Count: {followerCount}")
        time.sleep(5)
        action = webdriver.ActionChains(self.browser)
        time.sleep(5)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)

            newCount = len(dialog.find_elements_by_css_selector("li"))
            if followerCount != newCount:
                followerCount = newCount
                print(f"secondCount: {newCount}")
                time.sleep(5)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)

    def SearchHasthag(self,hasthag):
        self.browser.get(f"https://www.instagram.com/explore/tags/{hasthag}/")
        time.sleep(5)
        NumberOfPosts = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/div[2]/span/span')
        FollowHasthag = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/button')
        amI =FollowHasthag.text
        if amI == "Takiptesin":
            print("Zaten Takiptesin.")
        else:
            FollowHasthag.click()
        print(f"Number of Post: {NumberOfPosts.text}")


instagram = Instagram(username,password)
instagram.sıgnIn()
instagram.getFollowers()
instagram.SearchHasthag("NBA")
instagram.follow("Galatasaray")
instagram.unfollow("Galatasaray")