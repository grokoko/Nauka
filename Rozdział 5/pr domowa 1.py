#program wypisujący elementy listy w randomowej kolejności
import random

lista = ["jeden", "dwa", "trzy", "cztery"]
nowa_lista = []

while len(nowa_lista) != len(lista):
    word = random.choice(lista)
    if word not in nowa_lista:
        nowa_lista.append(word)

print(nowa_lista)






input("\n\nEnter")
