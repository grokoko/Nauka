#Gra w której komputer wybiera losowe słowo do odgadnięcia
#Gracz ma 5 prób.

import random

#słowa do wyboru:
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
#wybór słowa:
word = random.choice(WORDS)
#zmienna służąca do sprawdzenia czy odpowiedź jest poprawna:
correct = word

# Rozpoczęcie:
print(
    """
                Witaj w grze 'Odgadnij słowo'!
    Twoim celem jest odgadnięcie słowa wybranego przez system.
Jako podpowiedź będziesz znał ilośc liter w tym słowie. Możesz też 5 razy zapytać
czy dana litera znajduje się w wybranym słowie. Potem musisz wpisać odpowiedź.
Powodzenia !
"""
    )
print("Odgadywane słowo składa się z", len(word), "liter.")

tries = 1

while tries < 6:
    guess = input("\nPodaj literę: ")
    if guess.lower() in word:
        print("Ta litera znajduje się w odgadywanym słowie")
    else:
        print("Ta litera nie znajduje się w odgadywanym słowie")
    tries += 1
    
guess2 = input("\nPodaj słowo: ")
if guess2 == correct:
    print("Brawo! Zgadłeś! To słowo to:", word)
else:
    print("Przykro mi, to nie to słowo! :(")


input("\n\nEnter")
