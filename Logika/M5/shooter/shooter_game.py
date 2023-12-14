#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,player_width,player_height,speed):
        super().__init__()
        self.image = scale(load(image),(player_width,player_height))
        self.speed = speed

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed

    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > window_height:
            self.rect.y = 0
            self.rect.x=randint(80,window_width-80)
            lost = lost + 1

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.3)

font.init()

font1 = font.SysFont('Arial',36)




window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
background = scale(load('galaxy.jpg'),(window_width,window_height))

ship = Player('rocket.png',5,window_height-110,80,100,6)

monster = sprite.Group()
for i in range(5):
    mon = Enemy('ufo.png',randint(0,window_width-80),0,80,50,randint(1,5))
    monster.add(mon)


clock = time.Clock()
FPS = 60

game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    if not finish:
        window.blit(background,(0,0))
        txt_lose = font1.render(f'Пропущено: {lost}',True,(255,255,255))
        window.blit(txt_lose,(10,50))
        ship.reset()
        monster.draw(window)
        monster.update()

        ship.update()
    display.update()
    clock.tick(FPS)