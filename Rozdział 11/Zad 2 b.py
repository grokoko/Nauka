# Kryj się !
# Gracz musi uciekać przed spadającymi kamieniami

from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Player(games.Sprite):
    """ Ludzik sterowany przez gracza """
    image = games.load_image("ludzik.bmp")

    def __init__(self):
        """ Inicjalizuj gracza i licznik puntków """
        super(Player, self).__init__(image = Player.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną X myszy """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        
        self.collision()

    def destroy(self):
        self.destroy()

    def collision(self):
        """ Sprawdź czy kamień dotknął gracza """
        for stone in self.overlapping_sprites:
            stone.handle_hit()

    def handle_hit(self):
        """ Zniszcz gracza jeśli został trafiony """
        self.destroy()
        Stone.end_game(self)


class Stone(games.Sprite):
    """ Kamień który spada na ziemię """

    image = games.load_image("kamien.bmp")
    speed = 1
    
    def __init__(self, x = 200, y = 0):
        super(Stone, self).__init__(image = Stone.image,
                                    x = x, y = y, dy = Stone.speed)

        self.time_till_drop = 0

    def update(self):
        self.check_fall()
        self.check_drop()


    def check_fall(self):
        """ Sprawdź czy kamień dotknął ziemi """
        if self.bottom > games.screen.height:
            self.destroy()



    def end_game(self):
        """ Zakończ grę. """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)    
    
    def check_drop(self):
        """ Zrzut kamieni """
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        else:
            new_stone = Stone(x = self.x)
            games.screen.add(new_stone)

            # ustaw margines na mniej więcej 30% wysokości kamienia, niezależnie od prędkości   
            self.time_til_drop = int(new_stone.height * 2 / Stone.speed) + 2  

def main():
    """ Uruchom grę """
    wall_image = games.load_image("sciana.jpg", transparent = False)
    games.screen.background = wall_image

    ludzik = Player()
    games.screen.add(ludzik)

    new_stone = Stone()
    games.screen.add(new_stone)

    games.mouse.is_visible - False

    games.screen.event_grab = True
    games.screen.mainloop()

# Jadymyu !
main()