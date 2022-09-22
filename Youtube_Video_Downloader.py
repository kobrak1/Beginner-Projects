import pytube
import sys


class Video_Downloader():
    try:    
    
        def __init__(self, link, filename='VideO', direction="C:/Users/Desktop/Youtube_Videos"):
            self.link=link
            self.filename=filename
            self.direction=direction
            self.download()
            self.process()
            self.exit()
        def download(self):
            video = pytube.YouTube(self.link)
            dv = video.streams.get_highest_resolution()
            dv.download(self.direction, self.filename)
        def process(self):
            print("Video successfully downloaded..")
            
        def exit(self):
            sys.exit()
        

    except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError):
        print("Connection error!(Make sure you entered link correctly.)")
a = input("Link:")
b = input("Filename:")
c = input("Save to:")
Video_Downloader(a,b,c)




