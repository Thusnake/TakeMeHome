import pygame

class Paper(pygame.sprite.Sprite):
  def __init__(self, startpos=(50,50)):
    pygame.sprite.Sprite.__init__(self, self.groups)
    self.pos = [0,0,0,0]
    self.image = pygame.image.load("images/paper.png")
    self.rect = pygame.Rect(10, 10, 5 , 5)
    self.catched = False

  def update(self, seconds):
    pass

