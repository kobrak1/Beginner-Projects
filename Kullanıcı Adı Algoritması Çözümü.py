import string

def get_username():
    return input('Username:')
list=list(string.punctuation)
list.remove('_')
func=lambda list, un: any(s in un for s in list)

while True:
    un=get_username()
    if len(un)>25 or len(un)<4:
        print('Username lenght must be between 4-25\nPlease enter a valid username!')
        continue
    else:
        if un[0] not in string.ascii_letters:
            print('The first character of your username should be a letter.\nPlease enter a valid username!')
            continue
        else:
            if func(list, un) == True:
                print("Your username can include only '_' not the other punctuations.\nPlease enter a valid username!")
                continue
            else:
                if un[-1] =='_':
                    print("Your username can not end with '_' .\nPlease enter a valid username!")
                    continue
                else:
                    print('Your username is valid.')



