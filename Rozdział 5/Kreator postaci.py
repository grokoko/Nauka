#Kreator postaci
#Gracz ma do dyspozycji 30pkt, które może rozdysponować
#między 4ry atrybuty: siła, zdrowie, mądrość, żręczność.
#Gracz może również odejmować pkt z powrotem do puli

atrybuty = []
points = 30
choice = None
while choice != "0":

    print(
    """
    Kreator postaci.
    Masz do dyspozycji 30pkt, które możesz rozdzielić między nastepujące
    cechy: sila, zdrowie, mądrość, zręczność.
    0 - zakończ
    1 - Wyświetl atrybuty
    2 - Dodaj punkty
    3 - Odejmij punkty
    """
    )

    choice = input("Wybierasz: ")
    print()

    # zakończ
    if choice == "0":
        print("Do widzenia,")

    # Wyświetl wszystkie atrybuty
    elif choice == "1":
        print("Pozostałe punkty: ", points, "\n")
        print("Atrybuty")
        print("Cecha\tWartość")
        for entry in atrybuty:
            cecha, wartosc = entry
            print(cecha, "\t", wartosc)
            
    # Dodaj punkty
    elif choice == "2":
        if points > 0:
            print("Pozostałe punkty: ", points)
            cecha = input("Podaj cechę: ")
            wartosc = int(input("Ile punktów chcesz dodać do tej cechy?"))
            entry = (cecha, wartosc)
            atrybuty.append(entry)
            points -= wartosc
        else:
            print("Za mało punktów!")
        
    # Odejmij punkty
    elif choice == "3":
        entry = input("Którą cechę chcesz usunąć?")
        if entry in atrybuty:
            atrybuty.remove(entry)
        else:
            print(entry, "Nie ma takiej cechy")
            
    # nieznana opcja
    else:
        print("Niestety,", choice, "nie jest prawidłowym wyborem.")
  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
