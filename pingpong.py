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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <= 650:
            self.rect.x += self.speed

rocket = Player('прямоугольник.png', 0, 0, 4, 20, 80)
rocket2 = Player('прямоугольник.png', 620, 480, 4, 20, 80)

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
    rocket.reset()
    rocket2.reset()
    ball.reset()
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
