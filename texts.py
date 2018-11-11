import pygame

font = pygame.font.Font(pygame.font.match_font('segoeui'), 72)
gameOverHealth = "You are morbidly depressed."
gameOverMoney = "You are morbidly bankrupt."

class Message:
  def __init__(self, text, duration=0): # 0 is indefinite
    self.text = text
    self.duration = duration
    self.elapsed = 0
    self.dead = False
    self.surface = font.render(self.text, True, (255,0,0))
    self.leftOffset = -font.size(self.text)[0]/2
    self.topOffset = -font.size(self.text)[1]/2

  def update(self, seconds):
    self.elapsed += seconds

  def reSurface(self, text):
    self.text = text
    self.surface = font.render(self.text, True, (0, 128, 0))
    self.leftOffset = -font.size(self.text)[0]/2
    self.topOffset = -font.size(self.text)[1]/2
