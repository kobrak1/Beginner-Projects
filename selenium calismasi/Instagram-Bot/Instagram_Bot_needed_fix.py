from selenium import webdriver
from instagramUserInfo import username, password
from selenium.webdriver.common.keys import Keys
import time

class IG:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(chromedriver.exe, chrome_options= self.browserProfile)
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        self.browser.window_maximize()
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
    def getFollowers(self,max):
        self.browser.get(f'https://www.instagram.com/accounts/login/{self.username}/')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[3]/a/span').click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector('div[role=dialog] ul')
        followerCount = len(self.browser.find_element_by_css_selector('li'))

        print(f'first count: {followerCount}')
        action = webdriver.ActionChains(self.browser)

        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(self.browser.find_element_by_css_selector('li'))

            if followerCount != newCount:
                followerCount = newCount
                print(f'secon count: {newCount}')
                time.sleep(2)
            else:
                break
        followers = self.browser.find_element_by_css_selector('li')
        followerList = []
        i=0

        for user in followers:
            link= user.find_element_by_css_selector('li')
            followerList.append(link)
            i+=1
            if i == max:
                break

        with open('shit file.txt','w',encoding='UTF-8') as file:
            for item in followerList:
                file.write(item + '\n')

    def followUser(self,username):
        self.browser.get('https://www.instgram.com/'+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/button').click()
        if followButton.text != 'Following':
            followButton.click()
            time.sleep(2)
        else:
            print('Zaten takiptesin..')

    def unfollowUser(self,username):
        self.browser.get('https://www.instgram.com/'+ username)
        time.sleep(2)

        if followButton.text == 'Following':
            followButton.click()
            time.slep(2)
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
        else:
            print('Zaten takip etmiyorsun..')

        
instagram = IG(username,password)
instagram.signIn()
instagram.getFollowers(40)
instagram.followUser()
instagram.unfollowUser()
