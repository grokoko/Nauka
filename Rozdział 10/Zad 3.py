# Złóż zamowienie !
# Przykładowe menu jadłodajni z wielokrotną opcją wyboru
# i podliczeniem całości kosztu

from tkinter import *

class Menu(Frame):
    """ Aplikacja odzwierciedlająca restauracyjne menu.
    Można zamawiać różne potrawy czy napoje i dowiedzieć się
    od razu ile wyniesie całkowity koszt. """
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Utwórz widżety służące do wyboru potraw. """
        # Etykieta z opisem
        Label(self,
            text = "Wybierz to co byś chciał zamówić."
            ).grid(row = 0, column = 0, sticky = W)

        # Etykieta z instrukcją
        Label(self,
            text = "Dolne okienko wyświetli sume pieniędzy do zapłaty"
            ).grid(row = 1, column = 0, sticky = W)

        # Pola wyboru jedzenia
        self.kebab = BooleanVar()
        Checkbutton(self,
                    text = "Kebab - 15zl",
                    variable = self.kebab,
                    command = self.update_price
                    ).grid(row = 2, column = 0, sticky = W)

        self.pizza = BooleanVar()
        Checkbutton(self,
                    text = "Pizza - 20zl",
                    variable = self.pizza,
                    command = self.update_price
                    ).grid(row = 3, column = 0, sticky = W)

        self.hamburger = BooleanVar()
        Checkbutton(self,
                    text = "Hamburger - 10zl",
                    variable = self.hamburger,
                    command = self.update_price
                    ).grid(row = 4, column = 0, sticky = W)

        self.cheeseburger = BooleanVar()
        Checkbutton(self,
                    text = "Cheeseburger - 11zl",
                    variable = self.cheeseburger,
                    command = self.update_price
                    ).grid(row = 5, column = 0, sticky = W)

        self.pierogi = BooleanVar()
        Checkbutton(self,
                    text = "Pierogi - 14zl",
                    variable = self.pierogi,
                    command = self.update_price
                    ).grid(row = 6, column = 0, sticky = W)

        self.placki = BooleanVar()
        Checkbutton(self,
                    text = "Placki - 12zl",
                    variable = self.placki,
                    command = self.update_price
                    ).grid(row = 7, column = 0, sticky = W)

        self.cola = BooleanVar()
        Checkbutton(self,
                    text = "Cola - 6zl",
                    variable = self.cola,
                    command = self.update_price
                    ).grid(row = 8, column = 0, sticky = W)

        self.herbata = BooleanVar()
        Checkbutton(self,
                    text = "Herbata - 5zl",
                    variable = self.herbata,
                    command = self.update_price
                    ).grid(row = 9, column = 0, sticky = W)

        self.kawa = BooleanVar()
        Checkbutton(self,
                    text = "Kawa - 9zl",
                    variable = self.kawa,
                    command = self.update_price
                    ).grid(row = 10, column = 0, sticky = W)

        self.piwo = BooleanVar()
        Checkbutton(self,
                    text = "Piwo - 8zl",
                    variable = self.piwo,
                    command = self.update_price
                    ).grid(row = 11, column = 0, sticky = W)

        # Utwórz pole tekstowe do wyświetlania wyników
        self.price_txt = Text(self, width = 40, height = 5)
        self.price_txt.grid(row = 12, column = 0, columnspan = 3)

    def update_price(self):
        """ Zaktualizuj pole tekstowe z łączną ceną wybranych produktów. """
        price = 0

        if self.kebab.get():
            price += 15

        if self.pizza.get():
            price += 20

        if self.hamburger.get():
            price += 10

        if self.cheeseburger.get():
            price += 11

        if self.pierogi.get():
            price += 14

        if self.placki.get():
            price += 12

        if self.cola.get():
            price += 6

        if self.herbata.get():
            price += 5

        if self.kawa.get():
            price += 9

        if self.piwo.get():
            price += 8

        # Wyświetl wyniki
        price2 = str(price) + "zł"
        self.price_txt.delete(0.0, END)
        self.price_txt.insert(0.0, price2)

# część główna
root = Tk()
root.title("Menu")
app = Menu(root)
root.mainloop()