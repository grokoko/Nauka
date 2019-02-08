# Jaka to liczba z GUI
# Zadanie z 3iego rozdziału z dodanym interfejsem

from tkinter import *
import random

class Application(Frame):
    """Aplikacja z GUI. Program wybiera losową liczbę,
    a użytkownik ma pięć szans na zgadnięcie.
    """

    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.the_number = random.randint(1, 100)

    def create_widgets(self):
        """ Utwórz widżety potrzebne do pobrania informacji podanych przez 
        użytkownika i wyświetlania opowiadania.
        """
        # utwórz etykietę z instrukcją
        Label(self, 
        text = """Witaj w grze 'Jaka to liczba?' 
        Mam na myśli pewną liczbę od 1 do 100.
        Masz 5 podejść."""
            ).grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = W)

        # utwórz etykietę i pole znakowe służące do wpisania liczby
        Label(self,
        text = "Liczba: "
            ).grid(row = 3, column = 0, sticky = W)
        self.digit = Entry(self)
        self.digit.grid(row = 3, column = 1, sticky = W)

        # Utwórz przycisk akceptacji danych
        Button(self,
        text = "Kliknij, aby sprawdzić czy masz rację",
        command = self.check
        ).grid(row = 4, column = 0, sticky = W)

        self.answer = Text(self, width = 50, height = 5, wrap = WORD)
        self.answer.grid(row = 5, column = 0, columnspan = 2)  

    def check(self):
        """Wpisz w pole tekstowe odpowiedzi dla użytkownika"""
        # Pobierz wartości z interfejsu GUI
        guess = self.digit.get()
        guess = int(guess)

        # ustaw wartości początkowe
        self.tries = 5
        self.proby = 1
        answer1 = "Wygrałeś, ta liczba to", self.the_number, "Potrzebowałeś", self.proby, "prób!"

        # pętla zgadywania
        if guess == self.the_number:
            self.answer.insert(0.0, "Brawo, zgadłeś!\n")
        elif guess > self.the_number:
            self.answer.insert(0.0, "Za duża...\n") 
        else:
            self.answer.insert(0.0, "Za mała...\n")     

            guess = self.digit.get()
            guess = int(guess)
            self.tries -= 1
            self.proby += 1

      
        
# Część główna
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()