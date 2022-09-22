import random
import string
import time

print('*'*40+' Nickname Generator '+'*'*40)
print('Enter your nickname type.\n 1-Just Lowercase\n 2-Just Uppercase\n')
try:
    choice = str(input())


except:
    print('The answer must be numeric.')

time.sleep(1)

if choice == '1':
    print('You chose "Just Lowercase" nickname type.')

else:
    print('You chose "Just Uppercase" nickname type.')
time.sleep(1)

doc = []
i = 0

if choice == '1':
    list = string.ascii_lowercase
if choice=='2':
    list = string.ascii_uppercase


while i<15:
    x = random.randint(4,8)
    name = ''.join(random.sample(list, x))
    doc.append(name)
    i+=1

    if i==15:
        print(doc)
    else:
        pass
with open('dosya.txt','w') as d:
    d.write(', '.join(doc))

#comment line added