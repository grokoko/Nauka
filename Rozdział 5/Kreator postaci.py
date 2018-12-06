#Kreator postaci
#Gracz ma do dyspozycji 30pkt, które może rozdysponować
#między 4ry atrybuty: siła, zdrowie, mądrość, żręczność.
#Gracz może również odejmować pkt z powrotem do puli

points = 30
sila = 0
zdrowie = 0
madrosc = 0
zrecznosc = 0
choice = None
while choice != "0":

    print(
    """
    Kreator postaci.
    Masz do dyspozycji 30pkt, które możesz rozdzielić między nastepujące
    cechy: sila, zdrowie, mądrość, zręczność.
    0 - zakończ
    1 - Wyświetl atrybuty
    2 - Zmień siłę
    3 - Zmień zdrowie
    4 - Zmień mądrość
    5 - Zmień zręczność
    """
    )

    choice = input("Wybierasz: ")
    print()

    # zakończ
    if choice == "0":
        print("Do widzenia.")

    # Wyświetl wszystkie atrybuty
    elif choice == "1":
        print("Pozostałe punkty: ", points, "\n")
        print("Atrybuty:\nSiła:", sila, "\nZdrowie:", zdrowie, \
              "\nMądrość:", madrosc, "\nZręczność:", zrecznosc)
            
    # SIŁA !
    elif choice == "2":
        if points >= 0 and points <= 30:
            print("Pozostałe punkty: ", points)
            choice = input("Wpisz '+' jeśli chcesz dodać punkty lub '-' jeśli odjąć:")
            if choice == "+":
                punkty = int(input("Ile punktów chcesz dodać?"))
                if punkty > points or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna liczba pkt to:", points)
                else:
                    sila += punkty
                    points -= punkty
            elif choice == "-":
                punkty = int(input("Ile punktów chcesz odjąć?"))
                if punkty > sila or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna wartość siły to:", sila)
                else:
                    sila -= punkty
                    points += punkty
        else:
            print("Za mało punktów!")
            choice = input("Wybierasz:")                  
                             
    # Zdrowie
    elif choice == "3":
        if points >= 0 and points <= 30:
            print("Pozostałe punkty: ", points)
            choice = input("Wpisz '+' jeśli chcesz dodać punkty lub '-' jeśli odjąć:")
            if choice == "+":
                punkty == int(input("Ile punktów chcesz dodać?"))
                if punkty > points or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna liczba pkt to:", points)
                else:
                    zdrowie += punkty
                    points -= punkty
            elif choice == "-":
                punkty = int(input("Ile punktów chcesz odjąć?"))
                if punkty > zdrowie or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna wartość zdrowia to:", zdrowie)
                else:
                    zdrowie -= punkty
                    points += punkty
        else:
            print("Za mało punktów!")
            choice = input("Wybierasz:")    
                             
    #Mądrość
    elif choice == "4":
        if points >= 0 and points <= 30:
            print("Pozostałe punkty: ", points)
            choice = input("Wpisz '+' jeśli chcesz dodać punkty lub '-' jeśli odjąć:")
            if choice == "+":
                punkty = int(input("Ile punktów chcesz dodać?"))
                if punkty > points or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna liczba pkt to:", points)
                else:
                    madrosc += punkty
                    points -= punkty
            elif choice == "-":
                punkty = int(input("Ile punktów chcesz odjąć?"))
                if punkty > madrosc or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna wartość zdrowia to:", madrosc)
                else:
                    madrosc -= punkty
                    points += punkty
        else:
            print("Za mało punktów!")
            choice = input("Wybierasz:")    

    #Zręczność
    elif choice == "5":
        if points >= 0 and points <= 30:
            print("Pozostałe punkty: ", points)
            choice = input("Wpisz '+' jeśli chcesz dodać punkty lub '-' jeśli odjąć:")
            if choice == "+":
                punkty = int(input("Ile punktów chcesz dodać?"))
                if punkty > points or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna liczba pkt to:", points)
                else:
                    zrecznosc += punkty
                    points -= punkty
            elif choice == "-":
                punkty = int(input("Ile punktów chcesz odjąć?"))
                if punkty > zrecznosc or punkty <= 0:
                    print("Podałeś złą wartość. Aktualna wartość zdrowia to:", zrecznosc)
                else:
                    zrecznosc -= punkty
                    points += punkty
        else:
            print("Za mało punktów!")
            choice = input("Wybierasz:")      
                             
    # nieznana opcja
    else:
        print("Niestety,", choice, "nie jest prawidłowym wyborem.")
  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
