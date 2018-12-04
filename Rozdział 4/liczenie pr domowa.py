#Program, który liczy za użytkownika i pozwala mu
#wybrać początek, koniec i odstęp

poczatek = int(input("Wprowadź liczbę początkową:"))
koniec = int(input("Wprowadź liczbę końcową:"))
koniec += 1
odstep = int(input("Wprowadź odstęp:"))

for i in range(poczatek, koniec, odstep):
    print(i, end=" ")

input("\n\nEnter")
