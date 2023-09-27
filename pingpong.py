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

ball = GameSprite('мяч.png', 350, 250, 4, 50, 50)

font.init()
font1 = font.SysFont('Arial', 36)
text_1 = font1.render('PLAYER 1 LOSE', True, (255, 0, 0))
text_2 = font1.render('PLAYER 2 LOSE', True, (255, 0, 0))

num_fire = 0
rel_time = False

speed_x = 3
speed_y = 3

game = True
finish = False

while game:
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill((160, 222, 153))
        ball.reset()
        racket.update_l()
        racket2.update_r()
        racket.reset()
        racket2.reset()
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        if ball.rect.x < 0:
            window.blit(text_1, (200, 200))  
            finish = True
        if ball.rect.x > 700:
            window.blit(text_2, (200, 200)) 
            finish = True  
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

