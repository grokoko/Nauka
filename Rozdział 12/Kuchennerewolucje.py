# Kuchenne rewolucje
# Prostsze Space Invaders

import random
from superwires import games, color

games.init(screen_width = 640, screen_height = 480 , fps = 50)

class Kucharz(games.Sprite):
    """ Kosmiczny Kucharz, którego trzeba zniszczyć """
    image = games.load_image("Kucharz.bmp")

    speed = 0.1

    def __init__(self, x, y):
        super(Kucharz, self).__init__(
            image = Kucharz.image,
            x = x, y = y,
            dx = 0,
            dy = Kucharz.speed)

    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
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

class Ship(games.Sprite):
    image = games.load_image("statek.bmp")
    sound = games.load_sound("przyspieszenie.wav")
    VELOCITY = 0.2
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0

    def update(self): 
        if games.keyboard.is_pressed(games.K_LEFT):
            Ship.sound.play()
            self.dx -= Ship.VELOCITY
        if games.keyboard.is_pressed(games.K_RIGHT):
            Ship.sound.play()
            self.dx += Ship.VELOCITY

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

class Missile(games.Sprite):
    image = games.load_image("pocisk.bmp")
    sound = games.load_sound("pocisk.wav")
    BUFFER = 40
    LIFETIME = 100
    VELOCITY = 2

    def __init__(self, ship_x, ship_y):
        Missile.sound.play()

        buffer_y = Missile.BUFFER

        x = ship_x
        y = ship_y - buffer_y
        dx = 0
        dy = -Missile.VELOCITY

        super(Missile, self).__init__(image = Missile.image,
                                        x = x, y = y,
                                        dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        
def main():
    nebula_image = games.load_image("mglawica.jpg")
    games.screen.background = nebula_image

    for i in range(10):
        x = random.randrange(games.screen.width)
        y = 1
        new_chef = Kucharz(x = x, y = y)
        games.screen.add(new_chef)

    the_ship = Ship(x = games.screen.width/2,
                    y = games.screen.height - 15)
    games.screen.add(the_ship)
        

    games.screen.mainloop()

main()