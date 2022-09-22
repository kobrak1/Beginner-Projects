
import requests
import json
import time

print('Note: Write the currency abbreviations in capital letters!')
f = open("exchange.txt","w")
while True:
        
        print(" ")
        api_url = "https://api.exchangeratesapi.io/latest?base="
        a = str(input("Currency You Want to Convert:"))
        b= input("What currency will it be converted to?: ")
        amount=float(input("Amount:"))
        
        date=time.ctime()
        result = requests.get(api_url+a)
        if not result:
                print("No internet connection or some bullshit like that happened.")
        result=json.loads(result.text)
        total_amount = amount*result["rates"][b]
        print(f"{amount} {a} is equal to {total_amount} {b} in date: {date}")
        print(" ")
        print("%"*50)
       
        

        continue


