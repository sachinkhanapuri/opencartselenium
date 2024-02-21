import string
import random


def Genrandomstring(n):
    newstring=''
    for i in range(0,10):
        randomstring=random.choice(string.ascii_lowercase)
        print(randomstring,end='')
        newstring=newstring + randomstring
    emailgenr=newstring + "@gmail.com"
    return emailgenr


#print(Genrandomstring(10))

