from random import randint
import pygame
from app import *

class FloppyBird(App):
    def __init__(self):
        App.__init__(self, "images/floppy_bg.png")
        self.clock = pygame.time.Clock()
        self.x = 250
        self.y = 250
        self.speed_y = 0
        self.column_xlocation = 545
        self.column_ylocation = 0
        self.column_xsize = 80
        self.column_ysize = randint(0, 673)#0.7*height
        self.column_speed = 2
        self.score = 0

        self.sprite = pygame.image.load("images/floppy_bird.png")

    def Score(self, score):
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render("Memory collected: " + str(score), True, (0, 0, 0))
        self.screen.blit(self.text, [0, 0])

    def end(self):
        self.font = pygame.font.SysFont(None,30)
        self.text = self.font.render("Oh no! You ran out of memory", True, (255, 0 ,0))
        self.screen.blit(self.text, [120,250])

    def floppybird(self, x, y):
        self.screen.blit(self.sprite, [x-20,y-20])

    def column(self, x, y, xsize, ysize):
        pygame.draw.rect(self.screen, (0, 255, 0), [x,y,xsize, ysize])
        pygame.draw.rect(self.screen, (0, 255, 0), [x, int(y + ysize + 150), xsize, 962-ysize-150])#length*0.714

    def key(self, event):
        App.key(self, event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.speed_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.speed_y = 5;

    def run(self):
        App.run(self)
        self.column(self.column_xlocation, self.column_ylocation, self.column_xsize, self.column_ysize)
        self.Score(self.score)
        self.floppybird(self.x, self.y)
        self.column_xlocation -= self.column_speed
        self.y += self.speed_y
        if self.y > self.size[1] or self.y < 0:#~0.94*height
            self.end()
            self.column_speed = 0
            self.speed_y = 0
        if self.x > self.column_xlocation and self.x < self.column_xlocation + 3:
            self.score = self.score + 1

        if self.column_xlocation < -50:
            self.column_xlocation = 545
            self.column_ysize = randint(0, 673)#~0.7*height

        if self.x + 20 > self.column_xlocation and self.x + 20 < self.column_xlocation + self.column_xsize and (self.y + 20 > self.column_ysize+150 or self.y - 20 < self.column_ysize):
            self.end()
            self.column_speed = 0
            self.speed_y = 0

        
        pygame.display.flip()
        self.clock.tick(60)
