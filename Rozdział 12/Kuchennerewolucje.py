# Kuchenne rewolucje
# Prostsze Space Invaders

import random
from superwires import games, color

games.init(screen_width = 640, screen_height = 480 , fps = 50)

class Collider(games.Sprite):
    def update(self):      
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()               

    def die(self):
        """ Zniszcz się i pozostaw po sobie eksplozję. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()    

class Kucharz(Collider):
    """ Kosmiczny Kucharz, którego trzeba zniszczyć """
    image = games.load_image("Kucharz.bmp")

    speed = 1
    total = 0
    POINTS = 10

    def __init__(self, game, x, y):
        Kucharz.total += 1
        super(Kucharz, self).__init__(
            image = Kucharz.image,
            x = x, y = y,
            dx = 0,
            dy = Kucharz.speed)

        self.game = game

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

    def die(self):
        Kucharz.total -= 1
        self.game.score.value += int(Kucharz.POINTS)
        self.game.score.right = games.screen.width - 10  

        if Kucharz.total == 0:
            self.game.advance()

        super(Kucharz, self).die()

class Ship(Collider):
    image = games.load_image("statek.bmp")
    sound = games.load_sound("przyspieszenie.wav")
    VELOCITY = 5
    MISSILE_DELAY = 25

    def __init__(self, game, x, y):
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_LEFT):
            Ship.sound.play()
            self.dx -= Ship.VELOCITY
            if self.dx < -Ship.VELOCITY:
                self.dx = -Ship.VELOCITY
        if games.keyboard.is_pressed(games.K_RIGHT):
            Ship.sound.play()
            self.dx += Ship.VELOCITY
            if self.dx > Ship.VELOCITY:
                self.dx = Ship.VELOCITY

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

    def die(self):
        self.game.end()
        super(Ship, self).die()

class Missile(Collider):
    image = games.load_image("pocisk.bmp")
    sound = games.load_sound("pocisk.wav")
    BUFFER = 40
    LIFETIME = 100
    VELOCITY = 3

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
        super(Missile, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

class Explosion(games.Animation):
    sound = games.load_sound("eksplozja.wav")
    images = ["eksplozja1.bmp",
              "eksplozja2.bmp",
              "eksplozja3.bmp",
              "eksplozja4.bmp",
              "eksplozja5.bmp",
              "eksplozja6.bmp",
              "eksplozja7.bmp",
              "eksplozja8.bmp",
              "eksplozja9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()

class Game(object):
    def __init__(self):
        self.level = 0
        self.sound = games.load_sound("poziom.wav")

        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        self.ship = Ship(game = self, 
                        x = games.screen.width/2,
                        y = games.screen.height - 15)
        games.screen.add(self.ship)

    def play(self):
        games.music.load("temat.mid")
        games.music.play(-1)

        nebula_image = games.load_image("mglawica.jpg")
        games.screen.background = nebula_image

        self.advance()
        games.screen.mainloop()

    def advance(self):
        self.level += 1

        for i in range(10):
            x = random.randrange(games.screen.width)
            y = 1
            new_chef = Kucharz(game = self, x = x, y = y)
            games.screen.add(new_chef)

        level_message = games.Message(value = "Poziom " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        if self.level > 1:
            self.sound.play()

    def end(self):
        """ Zakończ grę. """
        # pokazuj komunikat 'Koniec gry' przez 5 sekund
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)


def main():
    kuchenne_rewolucje = Game()
    kuchenne_rewolucje.play()

main()