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
    kubki = [0]* ((b-a)+1) # tworzę możliwie najmnije kubełków
    for i in range(0,((b-a)+1)):
        kubki[i] = list.count(a+i) # przypisanie do pierwszego kubełka ilości najmniejszych wartości
    licznik = 0 # zmienna mówiąca nam o indeksach listy
    for i in range(0,((b-a)+1)): # sprawdzamy podany przedział
        for x in range(0,kubki[i]): # pętla zamieniające ineksy listy INDEKSAMI kubeczków w zależności od WARTOŚCI kubeczka
            list[licznik]=a+i
            licznik+=1
list1 =[]
#losowe liczby na potrzeby prób
for i in range(0,10000): # ilość danych
    #list1.append(random.randint(0,1000000))# zróżnicowanie danych
    list1.append(i)
#f=open("plik.txt") # otwarcie pliku
#for x in f:
 #   x = x.replace("\n", "")
 #   list1.append(int(x)) #dodawanie do listy elementów które są oddzielane znakiem /n czyli enterem(są w nowej lini)
print(list1)
list1.sort()
list1.reverse()
print(list1)
start = time.time()
#sortowanie_gnom(list1)
sortowanie_kubek(list1)
print(list1)
end = time.time()
total = end - start
zapis = open("wyniki.txt", "w")
zapis.write("Posortowane liczby z pliku plik.txt: \n")
#zapis wyników do pliku "wyniki"
for i in list1:
    zapis.write(str(i)+", ")
zapis.write("\nCzas ich sortowania(w sekundach) to: \n")
zapis.write(str(total))
print(total)
