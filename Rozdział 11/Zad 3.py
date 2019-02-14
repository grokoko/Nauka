# Prosty pong

from superwires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    """ Sprężysta pizza. """
    def update(self):
        """ Po osiągnięciu brzegu ekranu zmień wartość składowej prędkości na przeciwną. """ 
            
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.top < 0:
            self.dy = -self.dy

        if self.bottom > games.screen.height:
            self.game_over()

    def bounce(self):
        """ Odbij się od paletki """
        self.dy = -self.dy

    def game_over(self):
        """ Zakończ grę. """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 2 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)    

class Pan(games.Sprite):
    """
    Patelnia sterowana przez gracza służąca do łapania spadających pizz.
    """
    image = games.load_image("patelnia.bmp")

    def __init__(self):
        """ Initialize Pan object and create Text object for score. """
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Sprawdź, czy nie zostały złapane jakieś pizze. """
        for pizza in self.overlapping_sprites:
            pizza.bounce()

def main():
    wall_image = games.load_image("sciana.jpg", transparent = False)
    games.screen.background = wall_image

    pizza_image = games.load_image("pizza.bmp")
    the_pizza = Pizza(image = pizza_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 3,
                      dy = 3)
    games.screen.add(the_pizza)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()

# wystartuj!
main()