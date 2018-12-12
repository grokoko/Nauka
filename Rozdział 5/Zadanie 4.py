# Znajdź swojego dziadka
# Demonstruje używanie słowników

geek = {"Son Gohan": "Son Goku",
        "Trunks": "Vegeta",
        "Chi Chi" : "Byczy Lucyfer",
        "Pan" : "Son Gohan",
        "Junior" : "Piccolo",
        "16" : "Dr. Gero",
        "Son Goku" : "Son Gohan",
        "Vegeta" : "King Vegeta",
        }  

choice = None
while choice != "0":

    print(
    """
    Znajdź dziadka (gdzie to możliwe):
    
    0 - zakończ
    1 - znajdź dziadka
    2 - dodaj nowego syna
    3 - zmień przypasowanie ojca
    4 - usuń termin
    5 - Pokaż zasób słownika
    """
    )
    
    choice = input("Wybierasz: ")
    print()

    # wyjdź
    if choice == "0":
        print("Żegnaj.")

    # pobierz definicję
    elif choice == "1":
        term = input("Komu mam znaleźć dziadka? ")
        if term in geek:
            definition = geek[term]
            dziadek = geek[definition]
            print("\n", term, "jest wnukiem", dziadek)
        else:
            print("\nNiestety, nie znam takiej osoby", term)

    # dodaj parę termin-definicja
    elif choice == "2":
        term = input("Jaką osobę mam dodać?: ")
        if term not in geek:
            definition = input("\nPodaj ojca tej osoby: ")
            geek[term] = definition
            print("\nTermin", term, "został dodany.")
        else:
            print("\nTa osoba już istnieje!")

    # zmiana definicji istniejącego terminu
    elif choice == "3":
        term = input("Jaką parę mam zmienić?: ")
        if term in geek:
            definition = input("Kim jest nowy ojciec?: ")
            geek[term] = definition
            print("\nOjciec", term, "został zmieniony.")
        else:
            print("\nTen termin nie istnieje! Spróbuj go dodać.")
       
    # usunięcie pary termin-definicja
    elif choice == "4":
        term = input("Jaką parę mam usunąć?: ")
        if term in geek:
            del geek[term]
            print("\nOK, usunąłem", term)
        else:
            print("\nNie mogę tego zrobić! Tej osoby", term, "nie ma w słowniku.")

    # wyświetlnie zawartości słownika
    elif choice == "5":
        print(geek.items())

    # nieznana opcja
    else:
        print("\nNiestety,", choice, "to nieprawidłowy wybór.")
  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
