#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__()
        self.image = scale(load(image),(65,65))
        self.speed = speed

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= window_width - 80:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

wall1 = Wall(100, 100, 20, 150)
wall2 = Wall(300, 200, 20, 150)
wall3 = Wall(500, 300, 20, 150)

window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
background = scale(load('background.jpg'),(window_width,window_height))

player = Player('hero.png',5,420,4)
monster = Enemy('cyborg.png',620,300,2)
final = GameSprite('treasure.png',620,420,0)
game = True
finish = False

clock = time.Clock()
FPS = 60

mixer.init()
money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

font.init()
f =font.Font(None, 70)
win = f.render("You win!", True, (255,215,0))
lose = f.render("You lose!", True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game == False 
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        monster.reset()
        final.reset()
    
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win,(200,200))
            money_sound.play()
        
        if sprite.collide_rect(player,wall1,wall2,wall3):
            finish = True
            window.blit(lose,(200,200))
            kick_sound.play()
        

        

    player.update()
    monster.update()
    display.update()
    clock.tick(FPS)