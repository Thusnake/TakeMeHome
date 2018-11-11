from random import randint
import pygame
from app import *

class Clash(App):
  def __init__(self):
    App.__init__(self, "images/yelling_bg.png")

  def key(self, event):
    App.key(self, event)

  def run(self):
    App.run(self)

  def updateClashTimer(self, timer):
    pass
