from pygame import *

width = 600
height = 500

window = display.set_mode((width, height))
background_colour = (35, 94, 49)

clock = time.Clock()

game_over = False

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, s):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = s

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.bottom < height:
            self.rect.y += self.speed

    def update_2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed



player_1 = Player("racket.png", 0, 200, 50, 150, 4)
player_2 = Player("racket.png", 550, 200, 50, 150, 4)

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, s):
        super().__init__(img, x, y, w, h, s)
        self.speed_x = self.speed
        self.speed_y = self.speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

        if len(sprite.spritecollide(self, player_group, False)) != 0:
            self.speed_x *= -1


player_group = sprite.Group()
player_group.add(player_1)
player_group.add(player_2)
ball = Ball("tennnnis.png", 200, 200, 50, 50, 4)

while game_over == False:
    for e in event.get():
        if e.type == QUIT:
            game_over = True

    window.fill(background_colour)
    player_group.draw(window)
    ball.draw()

    player_1.update_1()
    player_2.update_2()
    ball.update()
    display.update()
    clock.tick(60)