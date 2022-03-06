#!/usr/bin/env python


# dodawanie , znajdowanie i usuwanie produktu

# produkty = {klucz : liczba kcal/100g }

produkty = {}

while (True):
    print ("1 : Dodaj produkt")
    print ("2 : Znajdz produkt")
    print ("3 : Usuń produkt")
    print ("4 : Zakończ")

    wybór = input ("Co chcesz zrobić? ")

    if (wybór == "1"):
        klucz = input("Podaj nazwę produktu, który chcesz dodać do listy: ")
        kaloryka = input ("Podaj liczbe kalorii produktu na 100 g : ")
        produkty [klucz] = kaloryka
        print ("Produkt dodany pomyślnie.")
        print(produkty[kaloryka])
    elif (wybór == "2"):
        klucz = input (" Podaj nazwę produktu, którego szukasz: ")
        if klucz in produkty:
            print (produkty [klucz])
        else:
            print ("Nie znaleziono produktu o nazwie: ", klucz)
    elif (wybór == "3"):
        klucz = input ("Jaki produkt chcesz usunąć? ")
        if klucz in produkty:
            del produkty[klucz]
            print ("Usunięto produkt o nazwie: ", klucz)
        else:
            print ("Nie znaleziono produktu o nazwie: ", klucz)
    elif (wybór == "4"):
        print ("Dbaj o siebie, licz dalej!:)")
        break
    else:
        print ("Podany produkt nie widnieje na liście produktów.")



#  nazwa produktu podana z ilością kalorii na 100g oraz ilościa węglowodanów , tłuszczów i białek na 100g
#  możliwość obliczenia ilości kalorii na podana gramaturę
#  mozliwość obliczenia gramatury białek, tłuszczow i węglowodanów na podaną liczbę kalorii
#  możliwość tworzenia własnych dań z obliczeniem ilości kalorii na danie oraz na 100g dania
#  kalkulator BMI wraz z interpretacją wyniku 
#  zwrócić uwagę na małe i duże litery
#  wyszukiwanie po wprawadzanych znakach
#  wyświetl liste produktów


 
