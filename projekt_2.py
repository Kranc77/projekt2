import os
import random # biblioteka dzięki której będziemy renderować losowe liczby
#def sortowanie_gnom(list):


#def sortowanie_kubek(list):

''' for x in f:
    x = x.replace("\n", "")
    list1.append(int(x)) #dodawanie do listy elementów które są oddzielane znakiem /n czyli enterem(są w nowej lini) '''
list1 =[]
for i in range(0,100):
    list1.append(random.randint(0,100))
print(list1)