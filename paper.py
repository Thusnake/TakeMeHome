import pygame
import numpy
import os
from coordinates import *

class Image(pygame.sprite.Sprite):
  def __init__(self, startpos=(1000,50), imgpath="images/paper.png"):
    pygame.sprite.Sprite.__init__(self)
    self.pos = [0,0,0,0]
    self.pos[0] = startpos[0] * 1.0
    self.pos[1] = startpos[1] * 1.0
    self.image = pygame.image.load(imgpath).convert_alpha()
    self.rect = self.image.get_rect()
    self.destination = []
    self.dead = False

  def update(self, seconds):
    # If some destination is set.
    if len(self.destination) > 1:
      self.pos[0] -= (self.pos[0] - self.destination[0]) / 5
      self.pos[1] -= (self.pos[1] - self.destination[1]) / 5
      self.pos[0] -= numpy.sign(self.pos[0] - self.destination[0]) * 3
      self.pos[1] -= numpy.sign(self.pos[1] - self.destination[1]) * 3
      if numpy.sqrt((self.pos[0] - self.destination[0])**2 + (self.pos[1] - self.destination[1])**2) < 4:
        self.pos[0:2] = self.destination
        self.destination = []

    self.rect.centerx = round(self.pos[0], 0)
    self.rect.centery = round(self.pos[1], 0)

  def onClicked(self):
    pass

class Paper(Image):
  def __init__(self):
    Image.__init__(self, PAPER_STACK, "images/paper.png")
    self.destination = PAPER
    self.stamped = False
    self.thrashed = False
    self.alpha = 0
    try:
        self.sound = pygame.mixer.Sound(os.path.join('.', 'throwPaperSound.wav'))
    except:
        raise UserWarning("Coudn't load the throw paper sound")

  def onClicked(self):
    self.destination = BIN_OPENING
    self.sound.play()
    self.thrashed = True

  def update(self, seconds):
    Image.update(self, seconds)
    if self.thrashed:
      self.image = pygame.transform.scale(self.image, (round(self.image.get_width() * 9/10) - 1, round(self.image.get_height() * 9/10) - 1))
      self.rect.centerx += 350
      self.rect.centery += 200
      if self.image.get_width() <= 10 or self.image.get_height() <= 10:
        self.thrashed = False
        self.dead = True

class PaperStack(Image):
  def __init__(self):
    Image.__init__(self, PAPER_STACK, "images/papers_stack.png")
    self.paperBuffer = None
    try:
        self.sound = pygame.mixer.Sound(os.path.join('.', 'paperFromStackSound.wav'))
    except:
        raise UserWarning("Coudn't load the stamp sound")

  def onClicked(self):
    self.paperBuffer = Paper()
    self.sound.play()


  def getPaper(self):
    paper = self.paperBuffer
    self.paperBuffer = None
    return paper

class Desk(Image):
  def __init__(self):
    Image.__init__(self, DESK, "images/table.png")

class Bin(Image):
  def __init__(self):
    Image.__init__(self, BIN, "images/bin.png")

class TablePhone(Image):
  def __init__(self):
    Image.__init__(self, PHONE, "images/phone_table.png")

class Stamp(Image):
  def __init__(self):
    Image.__init__(self, STAMP, "images/stamp.png")
    try:
        self.sound = pygame.mixer.Sound(os.path.join('.', 'stampSound.wav'))
    except:
        raise UserWarning("Coudn't load the stamp sound")
  def onClicked(self):
    self.destination = STAMP
    self.pos[0:2] = PAPER
    self.sound.play()

class ClashApp(Image):
  def __init__(self):
    Image.__init__(self, APPL1, "images/yelling_icon.png")

class HornApp(Image):
  def __init__(self):
    Image.__init__(self, APPR1, "images/hp_icon.png")

class FloppyApp(Image):
  def __init__(self):
    Image.__init__(self, APPL2, "images/floppy_bird_icon.png")

class Heart(Image):
  def __init__(self):
    Image.__init__(self, HEART, "images/heart.png")

class HappyBar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite
       with a given bossnumber, the Lifebar class can 
       identify the boos (Bird sprite) with this codeline:
       Bird.birds[bossnumber] """
    def __init__(self, health):
      if health < 0 or health > 100:
        health = 100
      pygame.sprite.Sprite.__init__(self)
      self.maxhealth = 100
      self.oldHealth = 100
      self.newHealth = 100
      self.health = health
      self.paint()
        
    def paint(self):
      self.image = pygame.Surface((700, 300))
      self.image.set_colorkey((0,0,0)) # black transparent
      self.rectangle = pygame.draw.rect(self.image, (0,255,0), (HAPPYBAR[0],HAPPYBAR[1],self.health * 4,100),0)
      self.rect = self.image.get_rect()

