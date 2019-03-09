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
    VELOCITY = 1

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
        
def main():
    nebula_image = games.load_image("mglawica.jpg")
    games.screen.background = nebula_image

    for i in range(10):
        x = random.randrange(games.screen.width)
        y = 1
        new_chef = Kucharz(x = x, y = y)
        games.screen.add(new_chef)

    the_ship = Ship(image = Ship.image,
                    x = games.screen.width/2,
                    y = games.screen.height - 15)
    games.screen.add(the_ship)
        

    games.screen.mainloop()

main()