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
        self.tries = 5
        self.proby = 1

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

        self.answer = Text(self, width = 70, height = 5, wrap = WORD)
        self.answer.grid(row = 5, column = 0, columnspan = 3)  

    def check(self):
        """Wpisz w pole tekstowe odpowiedzi dla użytkownika"""
        # Pobierz wartości z interfejsu GUI
        
        answer1 = "Wygrałeś, ta liczba to", self.the_number, "Potrzebowałeś", self.proby, "prób!\n"

        # pętla zgadywania
        try:
            guess = self.digit.get()
            guess = int(guess)
            if guess < 1 or guess > 100:
                self.answer.insert(0.0, "Podaj liczbę z przedziału 1 - 100!\n")
            elif self.tries < 1:            
                self.answer.insert(0.0, "Wykorzystałeś wszystkie próby\n")
            else:
                if guess == self.the_number:
                    self.answer.insert(0.0, answer1)
                    self.tries -= 1
                    self.proby += 1
                elif guess > self.the_number:
                    self.answer.insert(0.0, "Za duża...\n") 
                    self.tries -= 1
                    self.proby += 1
                else:
                    self.answer.insert(0.0, "Za mała...\n")  
                    self.tries -= 1
                    self.proby += 1   
        except ValueError:
            self.answer.insert(0.0, "To nie jest liczba!\n")
        
# Część główna
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()