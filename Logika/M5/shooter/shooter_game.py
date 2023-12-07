#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

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

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.3)

window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
background = scale(load('galaxy.jpg'),(window_width,window_height))

ship = Player('rocket.png',5,window_height-110,80,100,6)

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
        ship.reset()

        ship.update()
    display.update()
    clock.tick(FPS)