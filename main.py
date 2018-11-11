#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import random
from paper import *
from player import Player
from floppybird import *

WIDTH = 1920
HEIGHT = 1080

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#winstyle = 0  # |FULLSCREEN # Set the display mode
BIRDSPEED = 50.0

from texts import *

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
player = Player()

happinessBar = HappyBar(player.getHealth())
constantGroup = pygame.sprite.LayeredUpdates()
constantGroup.add(happinessBar, layer = '1')
face = HappyFace()
constantGroup.add(face, layer = '1')
constantGroup.add(Dollar(), layer = '1')

money = Message(str(player.getMoney()), 0)

workGroup = pygame.sprite.LayeredUpdates()
workGroup.add(Bin(), layer='1')
workGroup.add(Desk(), layer='2')
workGroup.add(TablePhone(), layer='3')
paperStack = PaperStack()
workGroup.add(paperStack, layer='3')
workGroup.add(Stamp(), layer='5')

phoneGroup = pygame.sprite.LayeredUpdates()
phoneGroup.add(ClashApp(), layer='3')
phoneGroup.add(HornApp(), layer='3')
phoneGroup.add(FloppyApp(), layer='3')

latestPaper = None
message = None
floppyBird = None

hornNotUsed = True

while mainloop:
  milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
  seconds = milliseconds / 1000.0 # seconds passed since last frame
  if isWorkBackground:
    player.decreaseHealth(seconds * 2)

  if player.getHealth() <= 0 :
    message = Message(gameOverHealth, 0)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop = False # pygame window closed by user
    elif floppyBird != None:
      floppyBird.key(event)
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

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if isWorkBackground: # Work inputs
        for sprite in workGroup.sprites():
          if sprite.rect.collidepoint(pygame.mouse.get_pos()):
            if isinstance(sprite,Paper) :
              print (sprite.stamped)
              if sprite.stamped : 
                player.increaseMoney(10)
              else : 
                player.decreaseMoney(20)
            elif isinstance(sprite,Stamp): 
              if latestPaper == None: # Stamp on table
                player.decreaseMoney(10)
              else:
                latestPaper.stamped = True # Stamp the paper
                latestPaper.image = pygame.image.load("images/rejected.png").convert_alpha()

            print (player.getMoney(), player.getHealth())
            sprite.onClicked()
            player.decreaseMoney(seconds * 30)
      else: # Phone inputs
        player.decreaseMoney(seconds * 30)
        money.reSurface(str(player.getMoney()))
        screen.blit(money.surface, [DOLLAR[0] + 75, DOLLAR[1] - 25])
        if phoneBackground == None: # There is no app open
          for sprite in phoneGroup.sprites():
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
              if isinstance(sprite, FloppyApp):
                phoneBackground = "images/floppy_bg.png"
                floppyBird = FloppyBird()
        elif phoneBackground == "images/hp_bg.png":
          pass
        elif phoneBackground == "images/yelling_bg.png":
          pass
        elif phoneBackground == "images/floppy_bg.png":
          pass
        else :
          for sprite in phoneGroup.sprites():
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
              if isinstance(sprite, HornApp) and hornNotUsed:
                player.resetHappiness()
                hornNotUsed = False
              elif isinstance(sprite, FloppyApp):
                # phoneBackground = pygame.image.load("images/floppy_bg.png")
                # phoneBackground.get_rect().centery = 540
                # phoneBackground.get_rect().centerx = WIDTH/2
                # phoneBackground = phoneBackground.convert()
                floppyBird = FloppyBird()

  # Update and remove the message if necessary
  if message != None:
    message.update(seconds)
    if message.duration != 0 and message.elapsed >= message.duration:
      message = None

  if floppyBird != None:
    floppyBird.run()
    screen.blit(floppyBird.screen, [690, 52])
    if floppyBird.done == 1:
      player.increaseHealth(floppyBird.score ** 2)
      floppyBird = None
  elif isWorkBackground :
    # Get the latest paper.
    paper = paperStack.getPaper()
    if paper != None:
      workGroup.add(paper, layer='4')
      latestPaper = paper
      
    # Remove all dead sprites.
    for element in workGroup.sprites():
      if element.dead:
        workGroup.remove(element)

    screen.blit(workBackground, (0,0))
    workGroup.clear(screen, workBackground)
    workGroup.update(seconds)
    workGroup.draw(screen)
  else:
    screen.blit(phoneBackground, (0,0))
    phoneGroup.clear(screen, phoneBackground)
    phoneGroup.update(seconds)
    phoneGroup.draw(screen)

  constantGroup.remove(happinessBar)
  constantGroup.remove(face)
  happinessBar = HappyBar(int(player.getHealth()))
  constantGroup.add(happinessBar, layer='1')
  if player.getHealth() > 70 :
    face = HappyFace()
  elif player.getHealth() > 30 :
    face = NeutralFace()
  else :
    face = SadFace()
  constantGroup.add(face, layer = '1')


  constantGroup.clear(screen, workBackground)
  constantGroup.update(seconds)
  constantGroup.draw(screen)

  money.reSurface(str(player.getMoney()))
  screen.blit(money.surface, [DOLLAR[0] + 75, DOLLAR[1] - 25])

  if message != None:
    screen.blit(message.surface, [WIDTH/2 + message.leftOffset, 250])

  pygame.display.flip()
