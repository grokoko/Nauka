# Jaka to liczba? Wersja z funkcją ask_number
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała
# czy prawidłowa

def instructions():
    print("\tWitaj w grze 'Jaka to liczba?'!")
    print("\nMam na myśli pewną liczbę od 1 do 100.")
    print("Masz 5 podejść.\n")   

def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def petla_while():
    while guess != the_number:
        if tries <= 1:
            break
        elif guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")    

        ask_number("Jaka to liczba?", 1, 100)
        tries -= 1
        proby += 1

    if tries <= 1:
        print("Przegrałeś, spróbuj jeszcze raz!")
    else:
        print("Wygrałeś, ta liczba to", the_number)
        print("Potrzebowałeś", proby, "prób!")
        
def main():
    import random
    instructions()
    
    # ustaw wartości początkowe
    the_number = random.randint(1, 100)
    guess = ask_number("Jaka to liczba?", 1, 100)
    tries = 5
    proby = 1

    # pętla zgadywania
    petla_while()


main()
input("\n\nEnter")
