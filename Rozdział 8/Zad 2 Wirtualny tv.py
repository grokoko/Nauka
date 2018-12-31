# Telewizor
# Można pozmieniać kanały i ustawić głośność

class Tv(object):
    """Wirtualny Tv"""
    def __init__(self, channel = 1, volume = 1):
        self.channel = channel
        self.volume = volume

    def change_channel(self, change):
        self.channel = change
        print("Kanał zmieniony na: ", change)

    def louder(self, loud = 1):
        self.volume += loud      
        if self.volume > 10:
            self.volume = 10
        print("Zwiększono moc dźwięku do: ", self.volume)  

    def turn_down(self, down = 1):
        self.volume -= down      
        if self.volume < 1:
            self.volume = 1
        print("Zmniejszono poziom dźwięku do: ", self.volume)  

def main():
    telewizor = Tv()

    choice = None  
    while choice != "0":
        print \
        ("""
        Wirtualny telewizor
    
        0 - zakończ
        1 - Zmień kanał
        2 - Podgłoś
        3 - Przycisz
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # Zmień kanał na wybrany przez siebie
        elif choice == "1":
            change = int(input("Jaki kanał wybierasz? Od 1 do 10: "))
            if change < 1:
                change = 1
            elif change > 10:
                change = 10            
            telewizor.change_channel(change)

        # Podgłoś
        elif choice == "2":
            telewizor.louder()
         
        # Przycisz
        elif choice == "3":
            telewizor.turn_down()

        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
