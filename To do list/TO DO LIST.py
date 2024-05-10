numer = 0
zadania = []

def przeslanie_zadan_z_pliku_do_listy():
    try:
        plik = open("zadania.txt")

        for line in plik.readline():
            zadania.append(line.strip())
        
        plik.close()
    except FileNotFoundError:
        return

def pokaz_zadania():
    indeks = 0

    for zadanie in zadania:
        print(zadanie + "[" + str(indeks) + "]")
        indeks += 1

def dodanie():
    wybor = 1
        
    while wybor == 1:
        print()
        zadanie = input("Podaj zadanie do dodanie: ")
        zadania.append(zadanie)
        print()
        print("Zadanie dodanie")
        print()
        print("1.Dodaj kolejne zadanie")
        print("2.Wroć do funkcji głównych")
        print()
        wybor = int(input("Wybierz następną funkcję: "))

def usuniecie():
    wybor_2 = 1
    
    while wybor_2 == 1:
        print()
        pokaz_zadania()
        usun = int(input("Podaj indeks zadania, które chcesz usunąć: "))
        if usun < 0 or usun > len(zadania) - 1:
            print("Takie zadanie nie istnieje")
            return

        else:
            zadania.pop(usun)
            print()
            print("Zadanie usunięte")
            print()
            print("1.Usuń kolejne zadanie z listy")
            print("2.Wróć do funkcji głównych")
            wybor_2 = int(input("Wybierz następną funkcję: "))

def zapisanie_do_pliku():
    plik = open("zadania.txt", "w")
    for zadanie in zadania:
        plik.write(zadanie+"\n")
    
    plik.close()

przeslanie_zadan_z_pliku_do_listy()

if numer < 5 or numer > 0:
    while numer != 5:
        print()  
        print("1.Pokaż zadania do wykonania")
        print("2.Dodaj zadania do wykonania")
        print("3.Usuń zadania")
        print("4.Zapisz zadania w pliku")
        print("5.Wyjdź z programu")
        print()
        numer = int(input("Podaj numer funkcji: "))
        
        if numer == 1:
            pokaz_zadania()
            
        if numer == 2:
            dodanie()
        
        if numer == 3:
            usuniecie()
        
        if numer == 4:
            zapisanie_do_pliku()
        
else:
    print("Taka funkcja nie istnieje.")