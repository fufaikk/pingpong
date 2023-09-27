from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
window.fill((160, 222, 153))


clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

racket = Player('прямоугольник.png', 100, 20, 4, 40, 100)
racket2 = Player('прямоугольник.png', 600, 400, 4, 40, 100)

ball = GameSprite('мяч.png', 350, 250, 4, 30, 30)

font.init()
font1 = font.SysFont('Arial', 36)
text_win = font1.render('YOU WIN', True, (0, 255, 0))
text_lose = font1.render('YOU LOSE', True, (255, 0, 0))

num_fire = 0
rel_time = False

game = True
finish = False

while game:
    if not finish:
        pass
    window.fill((160,222,153))
    ball.reset()
    racket.update_l()
    racket2.update_r()
    racket.reset()
    racket2.reset()
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
