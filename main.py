#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import random
from paper import *


pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
#winstyle = 0  # |FULLSCREEN # Set the display mode
BIRDSPEED = 50.0

def write(msg="pygame is cool"):
  myfont = pygame.font.SysFont("None", 32)
  mytext = myfont.render(msg, True, (0,0,0))
  mytext = mytext.convert_alpha()
  return mytext

background = pygame.Surface((screen.get_width(), screen.get_height()))
background.fill((255,255,255))     # fill white
background = background.convert()  # jpg can not have transparency
screen.blit(background, (0,0))     # blit background on screen (overwriting all)
clock = pygame.time.Clock()        # create pygame clock object 
mainloop = True
FPS = 60                           # desired max. framerate in frames per second. 

allgroup = pygame.sprite.Group()

Image.groups = allgroup

Bin()
Desk()
PaperStack()
Stamp()
Paper()

while mainloop:
  milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
  seconds = milliseconds / 1000.0 # seconds passed since last frame
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop = False # pygame window closed by user
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        mainloop = False # user pressed ESC
  # create new Paper on mouseclick
  if pygame.mouse.get_pressed()[0]:
    for sprite in allgroup.sprites():
      if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        sprite.onClicked()
  
  pygame.display.set_caption("[FPS]: %.2f birds: %i" % (clock.get_fps(), 0))

  allgroup.clear(screen, background)
  allgroup.update(seconds)
  allgroup.draw(screen)

  pygame.display.flip()
