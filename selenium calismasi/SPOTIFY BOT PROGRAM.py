from selenium import webdriver
import time
import os

print(os.getcwd())


url= "https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F"
driver = webdriver.Chrome()
def spotify_Login(url):

    
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    logIn_button = driver.find_element_by_xpath('//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/a').click()

    time.sleep(2)



def facebook_login():
    e_mail = driver.find_element_by_name("email")
    password = driver.find_element_by_name("pass")
    e_mail.send_keys("burakkarahan23@gmail.com")
    password.send_keys("hewal2323")
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    time.sleep(1)

def play_song():
    play_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button').click()
    time.sleep(1)

spotify_Login(url)
facebook_login()
play_song()
