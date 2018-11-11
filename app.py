from random import randint
import pygame

class App:
  def __init__(self, imageurl):
    self.size = (548, 962)
    self.screen = pygame.Surface(self.size)
    self.done = 0

    self.bg = pygame.image.load(imageurl)
    self.bg.get_rect().centery = 540
    self.bg = self.bg.convert()  # jpg can not have transparency

  def key(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        self.done = 1

  def run(self):
    self.screen.blit(self.bg, [0,0])
