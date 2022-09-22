from selenium import webdriver
import time


print('1-Twitter\n2-Instagram\n3-Facebook')
a = input('Kullanmak İstediğiniz Programı Seçiniz:')
    
if a == '1':
    x=input('Twitter Kullanıcı Adı: ')
    driver = webdriver.Chrome()
    url = "https://www.twitter.com/"
    driver.get(url+x)
    print(driver.title)
    time.sleep(200000)
elif a == '2':
    x=input('İnstagram Kullanıcı Adı: ')
    driver = webdriver.Chrome()
    url = "https://www.instagram.com/"
    driver.get(url+x+'/')
    print(driver.title)
    time.sleep(200000)
else:
    print("Not: Facebook kullanıcı adınızı yazarken isimler arasında  '-' kullanmayı unutmayınız.")
    x=input('Facebook Kullanıcı Adı: ')
    driver = webdriver.Chrome()
    url = "https://www.facebook.com/people/"
    driver.get(url+x)
    print(driver.title)
    time.sleep(200000)

    





        
        










