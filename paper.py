import pygame
import numpy

class Image(pygame.sprite.Sprite):
  def __init__(self, startpos=(1000,50), imgpath="images/paper.png"):
    pygame.sprite.Sprite.__init__(self, self.groups)
    self.pos = [0,0,0,0]
    self.pos[0] = startpos[0] * 1.0
    self.pos[1] = startpos[1] * 1.0
    self.image = pygame.image.load(imgpath)
    self.rect = self.image.get_rect()
    self.destination = []

  def update(self, seconds):
    # If some destination is set.
    if len(self.destination) > 1:
      self.pos[0] -= (self.pos[0] - self.destination[0]) / 5
      self.pos[1] -= (self.pos[1] - self.destination[1]) / 5
      self.pos[0] -= numpy.sign(self.pos[0] - self.destination[0]) * 2
      self.pos[1] -= numpy.sign(self.pos[1] - self.destination[1]) * 2
      if numpy.sqrt((self.pos[0] - self.destination[0])**2 + (self.pos[1] - self.destination[1])**2) < 4:
        self.pos[0:2] = self.destination
        self.destination = []

    self.rect.centerx = round(self.pos[0], 0)
    self.rect.centery = round(self.pos[1], 0)

  def onClicked(self):
    pass

class Paper(Image):
  def __init__(self):
    Image.__init__(self, (944.5, 759), "images/paper.png")

  def onClicked(self):
    self.destination = [270, 793]

class PaperStack(Image):
  def __init__(self):
    Image.__init__(self, (1805, 425), "images/papers_stack.png")

class Desk(Image):
  def __init__(self):
    Image.__init__(self, (1298.5, 838), "images/table.png")

class Bin(Image):
  def __init__(self):
    Image.__init__(self, (268, 959.5), "images/bin.png")

class Stamp(Image):
  def __init__(self):
    Image.__init__(self, (959.5, 35), "images/stamp.png")
