from selenium import webdriver
import time

link = 'https://www.instagram.com'

class instagram:
    def __init__(self,username,password):
        self.username='karaman7898'
        self.password='hewal2323'
    def signIn(self):
        self.browser = webdriver.Chrome(Chrome_Driver_Manager().install())
        self.browser.get(link)

        Username = self.browser.find_element_by_name('username')
        Password = self.browser.find_element_by_name('password')
        Username.send_keys(self.username)
        Password.senf_keys(self.password)

        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

ig = instagram('karaman7898','hewal2323')
ig.signIn()

