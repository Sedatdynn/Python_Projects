from githubUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class GitHub:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Desktop\chromedriver.exe")
        self.username = username
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]").click()

    def follow(self,user):
        user = self.browser.get(f"https://github.com/{user}")
        time.sleep(1)
        userProfile = self.browser.find_element_by_xpath("//*[@id='js-pjax-container']/div[2]/div/div[1]/div/div[4]/div[1]/div/div[1]/span/form[1]/input[2]").click()
    def loadFollowers(self):
        followers = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in followers:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)

    def getFollowers(self):
        self.browser.get(f"https://github.com/{username}?tab=followers")
        time.sleep(2)
        self.loadFollowers()


github = GitHub(username,password)
github.signIn()
github.getFollowers()
print("number of followers: "+ str(len(github.followers)))
print(github.followers)
github.follow("Sedatdynn")

