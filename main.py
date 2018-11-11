#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import random
from paper import *
from player import Player


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

workBackground = pygame.Surface((screen.get_width(), screen.get_height()))
workBackground.fill((255,255,255))     # fill white
workBackground = workBackground.convert()  # jpg can not have transparency
phoneBackground = pygame.image.load("images/phone_fullscreen.png")
phoneBackground.get_rect().centery = 540
phoneBackground = phoneBackground.convert()  # jpg can not have transparency
screen.blit(workBackground, (0,0))     # blit background on screen (overwriting all)
isWorkBackground = True
clock = pygame.time.Clock()        # create pygame clock object
mainloop = True
FPS = 60                           # desired max. framerate in frames per second.

workGroup = pygame.sprite.LayeredUpdates()
workGroup.add(Bin(), layer='1')
workGroup.add(Desk(), layer='2')
paperStack = PaperStack()
workGroup.add(paperStack, layer='3')
workGroup.add(Stamp(), layer='5')

phoneGroup = pygame.sprite.LayeredUpdates()
phoneGroup.add(ClashApp(), layer='3')
phoneGroup.add(HornApp(), layer='3')

player = Player()

while mainloop:
  milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
  seconds = milliseconds / 1000.0 # seconds passed since last frame
  player.decreaseHealth(seconds)
  print ("Health is {0} after decrease of {1}".format(player.getHealth(), seconds))
  if player.getHealth() <= 0 :
    print ("You are morbidly depressed")
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop = False # pygame window closed by user
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        mainloop = False # user pressed ESC
      elif event.key == pygame.K_SPACE:
        if isWorkBackground:
          screen.blit(phoneBackground, (0,0))
          isWorkBackground = False
        else :
          screen.blit(workBackground, (0,0))
          isWorkBackground = True

    # create new Paper on mouseclick
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      for sprite in workGroup.sprites():
        if sprite.rect.collidepoint(pygame.mouse.get_pos()):
          sprite.onClicked()

  if isWorkBackground :
    # Get the latest paper.
    paper = paperStack.getPaper()
    if paper != None:
      workGroup.add(paper, layer='4')

    workGroup.clear(screen, workBackground)
    workGroup.update(seconds)
    workGroup.draw(screen)
  else:
    phoneGroup.clear(screen, phoneBackground)
    phoneGroup.update(seconds)
    phoneGroup.draw(screen)

  pygame.display.flip()
