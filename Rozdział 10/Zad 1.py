# Mad Lib
# Tworzy opowiadanie oparte na szczegółach wprowadzonych przez użytkownika

from tkinter import *

class Application(Frame):
    """
    Aplikacja z GUI, która tworzy opowiadanie oparte na danych
    wprowadzonych przez użytkownika.
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
        text = "Wprowadź informację do nowego opowiadania"
        ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # utwórz etykietę i pole znakowe służące do wpisania imienia osoby
        Label(self,
        text = "Osoba: "
        ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        # utwórz etykietę i pole znakowe służące do wpisania przymiotnika
        Label(self,
        text = "Przymiotnik: "
        ).grid(row = 2, column = 0, sticky = W)
        self.adject_ent = Entry(self)
        self.adject_ent.grid(row = 2, column = 1, sticky = W)

        # utwórz etykietę i pole znakowe służące do wpisania wykonywanego zawodu
        Label(self,
        text = "Zawód: "
        ).grid(row = 3, column = 0, sticky = W)
        self.occupation_ent = Entry(self)
        self.occupation_ent.grid(row = 3, column = 1, sticky = W)     

        # Utwórz etykietę do pól wyboru przymiotników
        Label(self,
        text = "Przymiotnik(i): "
        ).grid(row = 4, column = 0, sticky = W)

        # Utwórz pole wyboru przymiotnika 'swędzące'
        self.is_itchy = BooleanVar()
        Checkbutton(self,
        text = "swędzące",
        variable = self.is_itchy
        ).grid(row = 4, column = 1, sticky = W)   

        # Utwórz pole wyboru przymiotnika 'gnijące'
        self.is_rotting = BooleanVar()
        Checkbutton(self,
        text = "gnijące",
        variable = self.is_rotting
        ).grid(row = 4, column = 2, sticky = W)  

        # Utwórz pole wyboru przymiotnika 'pocieszne'
        self.is_happy = BooleanVar()
        Checkbutton(self,
        text = "pocieszne",
        variable = self.is_happy
        ).grid(row = 4, column = 3, sticky = W)  

        # Utwórz etykietę i pole znakowe dla rzeczownika w liczbie mnogiej
        Label(self,
        text = "Rzeczownik w liczbie mnogiej: "
        ).grid(row = 5, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 5, column = 1, sticky = W)

        #Utwórz etykietę do pozostalych przycisków
        Label(self,
        text = "Inne: "
        ).grid(row = 6, column = 0, sticky = W)

        # Utwórz zmienna na inne:
        self.others = StringVar()
        self.others.set(None)

        # Utwórz przyciski opcji dla innych
        others = ["miecz", "koszulę", "paszport Polsatu"]
        column = 1
        for other in others:
            Radiobutton(self,
            text = other,
            variable = self.others,
            value = other
            ).grid(row = 6, column = column, sticky = W)
            column += 1

        # Utwórz etykietę i pole znakowane służące do wpisania czasownika
        Label(self,
        text = "Czasownik: "
        ).grid(row = 7, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 7, column = 1, sticky = W)

        # Utwórz przycisk akceptacji danych
        Button(self,
        text = "Kliknij, aby wyświetlić opowiadanie",
        command = self.tell_story
        ).grid(row = 8, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 9, column = 0, columnspan = 4)

    def tell_story(self):
        """ Wpisz w pole tekstowe nowe opowiadanie oparte na danych użytkownika. """
        # Pobierz wartości z interfejsu GUI
        person = self.person_ent.get()
        adjective = self.adject_ent.get()
        occupation = self.occupation_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_rotting.get():
            adjectives += "gnijące, "
        if self.is_itchy.get():
            adjectives += "swędzące, "
        if self.is_happy.get():
            adjectives += "pocieszne, "
        others = self.others.get()

        # create the story
        story = ""
        story += adjective 
        story += " badacz i "
        story += occupation
        story += " "
        story += person
        story += " o mało co nie zrezygnował z życiowej misji poszukiwania "
        story += "zaginionego miasta, które zamieszkiwały "
        story += noun
        story += ", gdy pewnego dnia "
        story += noun
        story += " znalazły "
        story += person + "a. "
        story += "Silne, "
        story += adjectives
        story += "osobliwe uczucie owładnęło badaczem. "
        story += "Po tak długim czasie poszukiwanie wreszcie się zakończyło. W oku "
        story += person + "a pojawiła się łza, która spadła na jego "
        story += others + ". "
        story += "A wtedy "
        story += noun
        story += " szybko pożarły "
        story += person + "a. "
        story += "Jaki morał płynie z tego opowiadania? Pomyśl, zanim zaczniesz coś "
        story += verb
        story += "."


        # Wyświetl opowiadanie
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

        
# Część główna
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()