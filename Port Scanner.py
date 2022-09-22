import socket 

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return

def main():
    ip=input('Target IP: ')
    for port in range(1,100):
        banner=retBanner(ip,port)
        if banner:
            print(f"[+] {ip} / {port} : {banner.strip}\n")
        else:
            print('no connection..')
main()





        