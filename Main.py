import pygame
import random
import os

pygame.init()

pygame.display.set_caption("MLCarGame")
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
DBLUE = (0,0,100)
GRAY = (125, 125, 125)
LBLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
HEIGHT = 465
clock = pygame.time.Clock()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WIDTH = 600
FPS = 60
dx= 0
g_speed = 1
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
m1,m2 =0,0


image_adress = os.path.join('images','car.png')
my_image = pygame.image.load(image_adress).convert_alpha()

image_adress = os.path.join('images','car1.png')
my_image1 = pygame.image.load(image_adress).convert_alpha()

image1_adress = os.path.join('images','mc.png')
mc_im = pygame.image.load(image1_adress).convert_alpha()


class car(pygame.sprite.Sprite):
    def __init__(self,x,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.x = x
        self.pos = pos
    def update(self,speed):
        y = 0
        if self.pos == 4:
            y = 45
        if self.pos == 3:
            y = 135
        if self.pos == 2:
            y = 255
        if self.pos == 1:
            y = 345
        if self.pos == 2 or self.pos == 4:
            self.x = self.x+speed
            screen.blit(my_image1,(self.x,y))
        if self.pos == 1 or self.pos == 3:
            self.x = self.x-speed
            screen.blit(my_image,(self.x,y))
        if self.x == 0 or self.x == WIDTH:
            self.pos = random.randint(1,4)
            if self.pos == 2 or self.pos == 4:
                self.x = 1
            if self.pos == 1 or self.pos == 3:
                self.x = WIDTH-1
        self.rect.x = self.x
        self.rect.y = y

class mc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.x = WIDTH/2
        self.y = 5
        
    def show(self):
        screen.blit(mc_im,(self.x,self.y))
    def motion(self,m1,m2):
        if self.x+m1 < WIDTH-2 and self.x+m1 > 2:
            self.x = self.x + m1
        if self.y+m2 < HEIGHT-2 and self.y+m2 > 2:
            self.y = self.y + m2
        self.rect.x = self.x
        self.rect.y = self.y


mc1 = mc()
def game_map():
    pygame.draw.line(screen, DBLUE, [0, 22.5], [WIDTH, 22.5], 45)
    pygame.draw.line(screen, DBLUE, [0, 442.5], [WIDTH, 442.5], 45)
    pygame.draw.line(screen, DBLUE, [0, 232.5], [WIDTH, 232.5], 45)

cars=[]
for i in range(4):
    x = random.randint(0,WIDTH)
    pos = random.randint(1,4)
    caar = car(x,pos)
    cars.append(caar)

while run:
    for i in range(len(cars)):
        if cars[i].rect.colliderect(mc1.rect):
            run=False
    screen.fill(WHITE)
    clock.tick(FPS)
    game_map()
    
    for i in range(len(cars)):
        cars[i].update(g_speed)
    mc1.show()
    mc1.motion(m1,m2)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                m1 = -1
                m2 = 0
            if i.key == pygame.K_DOWN:
                m1 = 0
                m2 = 1
            if i.key == pygame.K_RIGHT:
                m1 = 1
                m2 = 0
            if i.key == pygame.K_UP:
                m1 = 0
                m2 = -1
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_a, pygame.K_s, pygame.K_d,pygame.K_w]:
                m1,m2 = 0,0
    pygame.display.flip()
pygame.quit()
