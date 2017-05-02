#IMPORT

import pygame

#DEFINE

class Racket:
    def __init__(self,pos,size,ctrl_up,ctrl_down,side,move_speed=300):
        self.pos=pos
        self.size=size
        self.ctrl_up=ctrl_up
        self.ctrl_down=ctrl_down
        self.side=side
        self.move_speed=move_speed
        self.pos_1_old=self.pos[1] #pro výpočet rychlosti v parametru move()
    def draw(self):
        pygame.draw.rect(screen,pygame.Color(255,255,255),(self.pos[0],self.pos[1],self.size[0],self.size[1]))
    def move(self):
        if pygame.key.get_pressed()[self.ctrl_down]:
            self.pos[1]+=self.move_speed * deltatime
        if pygame.key.get_pressed()[self.ctrl_up]:
            self.pos[1]-=self.move_speed * deltatime
        self.speed=self.pos[1]-self.pos_1_old
    #if side=="l":

class Ball:
    def __init__(self,pos,size,speed,spin=0):
        self.pos=pos
        self.size=size
        self.speed=speed
        self.spin=spin
    def move(self):
        self.pos[0]+=self.speed[0]*deltatime
        self.pos[1]+=self.speed[1]*deltatime
    def draw(self):
        pygame.draw.rect(screen,pygame.Color(255,255,255),(self.pos[0],self.pos[1],self.size[0],self.size[1]))
    def collision(self,obj): #kolize s plošinami
        if (self.pos[0] < obj.pos[0] + obj.size[0]
        and self.pos[0] + self.size[0] > obj.pos[0]
        and self.pos[1] < obj.pos[1] + obj.size[1]
        and self.size[1] + self.pos[1] > obj.pos[1]):
            self.spin+=(self.speed[1]-obj.speed)/2 ######################## dodělat simulaci spinu
            self.speed[1]+=self.spin
            self.speed[0]*=-1
    def collision_sides(self): #kolize s okraji
        if self.pos[1] <= 0:
            self.speed[1]*=-1
        if self.pos[1] >= 600-self.size[1]:
            self.speed[1]*=-1

        

#INITIALISE

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("pong by matj1")

racket_left=Racket([32,236], [16,128], pygame.K_q, pygame.K_a,"l") #změna ovládání z ws na qa pro colemak
racket_right=Racket([752,236], [16,128], pygame.K_UP, pygame.K_DOWN,"r")
ball=Ball([388,288], [24,24], [300,0])

clock=pygame.time.Clock()

#show_fps=pygame.font.Font("consola.ttf",12) #pro zbrazení fps

pygame.init()

#LOOP

while True:
    deltatime=clock.tick(60)/1000

    racket_left.move()
    racket_right.move()
    ball.move()

    ball.collision(racket_left)
    ball.collision(racket_right)
    ball.collision_sides()
    
    racket_left.draw()
    racket_right.draw()
    ball.draw()

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        break

    pygame.display.flip()
    screen.fill(pygame.Color(0,0,0))
    pygame.event.pump()
