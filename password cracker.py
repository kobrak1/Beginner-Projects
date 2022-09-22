from string import ascii_lowercase
from random import sample
import sys
import re

# num=int(input('Decimal Places:'))
dosya=[]
lower_case=list(ascii_lowercase)

i=0
while i<100:
    sifre="".join(sample(lower_case,6))
    dosya.append(sifre)
        
    i+=1

sfr=open('sifreler.txt',"w")
for x in dosya:
    sfr.write(f'{x}\n')
    
print("başarılı bir şekilde aktarıldı.")

if 'karhan' in dosya:
    print('karhan is in the list..')
else:
    print('no match..')

sys.exit()

