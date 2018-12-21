# Rzut monetą
# Program "rzuca monetą" 100 razy, a następnie podaje liczbę orzłów i reszek

import random

#zmienne
orzeu = 0
reszka = 0
total = 0


#pętla while
while total < 100:
    moneta = random.randint(1,2)
    if moneta == 1:
        orzeu += 1
    else:
        reszka += 1
    total += 1

print("Liczba orląt to: ", orzeu, "a reszek to: ", reszka)
print("Łącznie", total, " rzutów.")

input("\n\nEnter")
