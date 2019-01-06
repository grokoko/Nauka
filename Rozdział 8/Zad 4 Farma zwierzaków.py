# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować
import random

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
    
    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name
        return rep

    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
    
    def eat(self, food):
        if food < 1:
            food = 1
        elif food > 4:
            food = 4
        print("Mniam, mniam.  Dziękuję za", food, "jedzenia.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        if fun  < 1:
            fun = 1
        elif fun > 4:
            fun = 4
        print("Hura! Dziękuje za wspólną zabawę przez", fun, "minuty")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    # Nadaj imiona zwierzakom
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    hunger = random.randint(1, 10)
    boredom = random.randint(1, 10)
    crit = Critter(crit_name, hunger, boredom)

    crit_name2 = input("Jak chcesz nazwać drugiego zwierzaka?: ")
    hunger = random.randint(1, 10)
    boredom = random.randint(1, 10)
    crit2 = Critter(crit_name2, hunger, boredom)

    crit_name3 = input("Jak chcesz nazwać trzeciego zwierzaka?: ")
    hunger = random.randint(1, 10)
    boredom = random.randint(1, 10)
    crit3 = Critter(crit_name3, hunger, boredom)

    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun farmy zwierzaków
    
        0 - zakończ
        1 - słuchaj swoich zwierzaków
        2 - nakarm swoje zwierzaki
        3 - pobaw się ze swoimi zwierzakami
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaków
        elif choice == "1":
            crit.talk()
            crit2.talk()
            crit3.talk()
        
        # nakarm swoje zwierzaki
        elif choice == "2":
            food = int(input("Ile jedzenia chcesz podać zwierzakom? (Od 1 do 4)"))
            crit.eat(food)
            crit2.eat(food)
            crit3.eat(food)
         
        # pobaw się ze swoimi zwierzakami
        elif choice == "3":
            fun = int(input("Jak długo chcesz się bawić ze zwierzakiem? (Od 1 do 4)"))
            crit.play(fun)
            crit2.play(fun)
            crit3.play(fun)

        # Ukryta opcja, która wyświetla konkretne wartości atrybutów obiektów
        elif choice == "4":
            print("Wyświetlenie wartości argumentów obiektu crit:")
            print("Imię: ", crit.name, "\nPoziom głodu: ", crit.hunger, "\nPoziom nudy: ", crit.boredom)
            print("\nWyświetlenie wartości argumentów obiektu crit2:")
            print("Imię: ", crit2.name, "\nPoziom głodu: ", crit2.hunger, "\nPoziom nudy: ", crit2.boredom)
            print("\nWyświetlenie wartości argumentów obiektu crit3:")
            print("Imię: ", crit3.name, "\nPoziom głodu: ", crit3.hunger, "\nPoziom nudy: ", crit3.boredom)

        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
