import string
liste=list(string.ascii_lowercase)
print(liste.index('x'),liste.index('q'),liste.index('w'))
del liste[23]
del liste[15]
del liste[20]
print(liste)