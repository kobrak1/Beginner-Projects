import pyqrcode

def burak(link,file_name):
    link=pyqrcode.create(link)
    link.png(f"{file_name}.png", scale=6)
link=str(input("Link:"))
file_name=input("File Name:")
burak(link,file_name)