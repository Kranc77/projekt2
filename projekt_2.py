import os
import time
import random # biblioteka dzięki której będziemy renderować losowe liczby
def sortowanie_gnom(list):
    pozycja = 0
    while(pozycja<len(list)): # pętla działa dopóki nie dojdziemy do ostatniego elementu
        if(pozycja==0 or list[pozycja]>=list[pozycja-1]):
            pozycja+=1 # gdy lista jest posortowana lub gdy mamy pozycje 0 czyli pierwszy el. listy to zwiększamy pozycję
        else:
            list[pozycja - 1],list[pozycja] = list[pozycja], list[pozycja-1] # w c++ musielibyśmy użyć tu funkcji "swap" albo wprowadzić nową zmienną pomocniczą o ile się nie mylę
            # a w pythonie jest takie właśnie proste obejście związane z zamianą pozycji,
            pozycja-=1 # gdy lista nie była posortowana i musieliśmy zamienić liczby w liście to musimy zmniejszyć pozycję
            # by sprawdzić czy zamieniona liczba jest w na odpowiednim miejscu

def sortowanie_kubek(list):
    a = min(list) # wykorzystałem funkcję min i max dostępne w pyhtonie
    b = max(list)
    kubki = [0]* (len(list)+1)
    for i in range(a,b+1):
        kubki[i]=list.count(i)
    print(kubki)
    licznik = 0 # zmienna mówiąca nam o indeksach listy
    for i in range(a,b+1): # sprawdzamy podany przedział
        for x in range(0,kubki[i]): # pętla zamieniające ineksy listy INDEKSAMI kubeczków w zależności od WARTOŚCI kubeczka
            list[licznik]=i
            licznik+=1
def sortowanie_kubek_v2(list,n):
    a = min(list)
    b = max(list)
    kubki = [n-1]
    for i in range(0,((b-a))):
        kubki[i]=list.count(i)
    print(kubki)
    licznik = 0
    for i in range(0, ((b - a) + 1)):
        for x in range(0,kubki[i]):
            list[licznik]=i
            licznik+=1
list1 =[]
for i in range(0,20):
    list1.append(random.randint(0,10))
print(list1)
start = time.time()
#sortowanie_gnom(list1)
sortowanie_kubek(list1)
print(list1)
end = time.time()
total = end - start
print(total)
