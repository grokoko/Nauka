# Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
# gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
# gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
# odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
# sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.
 
import random
 
print("\tWitaj!\n")
print("Program w którym komputer odgaduje liczbę z zakresu od 1 do 100.")
y = int(input("\nPomyśl o jakiejś liczbie (zapisz liczbę w pamięci): "))
x = random.randint(1, 100)
 
while x != y:
    x = random.randint(1, 100)
    if x == y:
        print("Twoja liczba to", x, "3maj się")
        break
    print("Czy miałeś na myśli liczbę", x, "?")
 
    reply = input("tak/nie: ")
    if reply == "tak":
        print("To jest oszustwo. To nie jest twoja prawdziwa liczba!!")
        break
 
input("\n\nAby zakończyć pracę programu naciśnij enter!")
