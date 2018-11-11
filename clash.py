from random import randint
import pygame
from app import *

class Clash(App):
  def __init__(self):
    App.__init__(self, "images/yelling_bg.png")
    self.font = pygame.font.Font(pygame.font.match_font('segoeui'), 72)

  def key(self, event):
    App.key(self, event)

  def run(self):
    App.run(self)

  def updateClashTimer(self, timer):
    self.surface = self.font.render(str(timer), True, (0, 128, 0))
    self.leftOffset = -self.font.size(str(timer))[0]/2
    self.topOffset = -self.font.size(str(timer))[1]/2
