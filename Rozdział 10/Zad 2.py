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
        guess1 = int(guess)

        # ustaw wartości początkowe
        the_number = random.randint(1, 100)
        tries = 5
        proby = 1
        answer1 = "Wygrałeś, ta liczba to", the_number, "Potrzebowałeś", proby, "prób!"

        # pętla zgadywania
        while guess1 != the_number:
            if tries <= 1:
                break
            elif guess1 > the_number:
                self.answer.delete(0.0, END)
                self.answer.insert(0.0, "Za duża...") 
            else:
                self.answer.delete(0.0, END)
                self.answer.insert(0.0, "Za mała...")     

            guess = self.digit.get()
            guess1 = int(guess)
            tries -= 1
            proby += 1

        if tries <= 1:
            self.answer.delete(0.0, END)
            self.answer.insert(0.0, "Przegrałeś, spróbuj jeszcze raz!") 
        else:
            self.answer.delete(0.0, END)
            self.answer.insert(0.0, answer1)
      
        
# Część główna
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()