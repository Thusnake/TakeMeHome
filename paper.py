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
    try:
        self.sound = pygame.mixer.Sound(os.path.join('.', 'throwPaperSound.wav'))
    except:
        raise UserWarning("Coudn't load the throw paper sound")

  def onClicked(self):
    self.destination = BIN_OPENING
    self.sound.play()

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
