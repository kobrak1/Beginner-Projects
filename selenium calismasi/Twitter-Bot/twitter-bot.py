from TwitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    def logIn(self):
        link = 'https://twitter.com/login'
        self.browser.get(link)
        self.browser.maximize_window()
        time.sleep(2)

        self.browser.find_element_by_name('session[username_or_email]').send_keys(self.username)
        self.browser.find_element_by_name('session[password]').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
        time.sleep(2)
    def serachBar(self,hashtag):
        Input = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        Input.send_keys(hashtag)
        time.sleep(2)

        Input = send_keys(Keys.ENTER)
        time.sleep(2)
        
        list = self.browser.find_element_by_xpath('//div[@data-testid="tweet"]/div[2]/div[2]')
        for item in list:
            print(item.text)




twttr = TwitterBot(username,password)
twttr.logIn()
twttr.serachBar('erdoğan')
        
        
