import random
import urllib.request
import requests


def Download():
        
        
        fileFormat = input('File Format:')
        url=input('url:')
        a = input('File Name:')
        print('Chose the file path:\n1-Masaüstü\n2-Videolar\n3-D Diski\n4-Dosya İndirme Programı\n5-Resimler\n6-Müzikler')
        x=input()
        
        if x=='1':
                x='/Users/ahmet.karhan2016/Desktop/'
        elif x=='2':
                x='/Users/ahmet.karhan2016/Videos/'
        elif x=='3':
                x='M:/'
        elif x=='4':
                x='/Users/ahmet.karhan2016/Desktop/Dosya Indirme Programı/'
        elif x=='5':
                x='/Users/ahmet.karhan2016/Pictures/'
        elif x=='6':
                x='/Users/ahmet.karhan2016/Music/'
        

        
        urllib.request.urlretrieve(url,f'{x}{a}.{fileFormat}')
                        
                                

        
        status=requests.get(url)
        print('Status Code:',status.status_code)
        print('Selected file downloaded on desktop sccessfully..')

Download()

