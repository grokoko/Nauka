# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
Za rozwiązanie zagadki w pierwszej próbie dostaniesz 10pkt, w drugiej 7pkt, a w 3ciej 4pkt.
Po trzech nieudanych próbach wyświetli się podpowiedź, jednak wtedy dostaniesz tylko 1pkt!
"""
)
print("Zgadnij, jakie to słowo:", jumble)

tries = 1
points = 10
guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    if tries >= 4:
        break
    if tries >= 3:
        print("Podpowiedź: Pierwsza litera to:", correct[0])
    guess = input("Twoja odpowiedź: ")
    tries += 1
    points -=3
    
if guess == correct:
    print("Zgadza się! Zgadłeś! Dostajesz:", points,"pkt!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
