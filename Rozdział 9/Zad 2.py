# Wojna
# Od 1 do 7 graczy

import kartydowojny, gry 

class War_Card(kartydowojny.Card):
    """ Karta do blackjacka. """

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
        return v

class War_Hand(kartydowojny.Hand):
    """ Ręka w wojnie. """

    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    @property     
    def total(self):
        # jeśli karta w ręce ma wartość None, to i wartość sumy wynosi None
        for card in self.cards:
            if not card.value:
                return None
        
        # zsumuj wartości kart
        t = 0
        for card in self.cards:
              t += card.value  
                
        return t

class Player(kartydowojny.Hand):
    def lose(self):
        print(self.name, "lose.")

    def win(self):
        print(self.name, "win.")

class Game(object):
    """ Gra w Wojnę. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = War_Hand(name)
            self.players.append(player)

        self.deck = kartydowojny.Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):

        # rozdaj każdemu po karcie
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players:
            print(player)

        # porównaj karty    
        scores = []
        for player in self.players:
            print(player, player.name, player.total)
            scores.append([player.total, player.name])

        scores.sort(reverse = True)

        print(scores[0][1], "wygrał z kartą: ", scores[0][0])

        for player in self.players:
            if player.name == scores[0][1]:
                player.win()
            else:
                player.lose()

        # usuń karty wszystkich graczy
        for player in self.players:
            player.clear()
            
        # Usuń talię i dodaj nową
        self.deck.clear()
        self.deck.populate()
        self.deck.shuffle()        

def main():
    print("\t\tWitaj w grze 'Wojna'!\n")
    
    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()
        
    game = Game(names)

    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")        