import os
import random # biblioteka dzięki której będziemy renderować losowe liczby
def sortowanie_gnom(list):
    pozycja = 0
    while(pozycja<len(list)): # pętla działa dopóki nie dojdziemy do ostatniego elementu
        if(pozycja==0 or list[pozycja]>=list[pozycja-1]):
            pozycja+=1 # gdy lista jest posortowana lub gdy mamy pozycje 0 czyli pierwszy el. listy to zwiększamy pozycję
        else:
            list[pozycja - 1],list[pozycja] = list[pozycja], list[pozycja-1] # w c++ musielibyśmy użyć tu funkcji "swap" albo wprowadzić nową zmienną pomocniczą o ile się nie mylę
            # a w pythonie jest takie właśnie proste obejście związane z zamianą pozycji,
            pozycja-=1 # gdy lista nie była posortowana i musieliśmy zamienić liczby w liście to musimy zmniejszyć pozycję by sprawdzić czy zamieniona liczba jest w na odpowiednim miejscu

def sortowanie_kubek(list):
    a = min(list)
    b = max(list)
    kubki = [0]* ((b-a)+1)
    print(a)
    print(b)
    for i in range(0,((b-a))):
        kubki[i]=list.count(i)
    print(kubki)
    list2 = []
    for i in range(0, ((b - a) + 1)):
        for x in range(0,kubki[i]):
            list2.append(i)
    print(list2)




''' for x in f:
    x = x.replace("\n", "")
    list1.append(int(x)) #dodawanie do listy elementów które są oddzielane znakiem /n czyli enterem(są w nowej lini) '''
list1 =[]
for i in range(0,100):
    list1.append(random.randint(0,100))
print(list1)
#sortowanie_gnom(list1)
#print(list1)
sortowanie_kubek(list1)
