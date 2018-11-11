class Player:
  def __init__(self):
    self.happiness = 1.0
    self.money = 1000.0

  def increaseHealth(self, amount):
   self.happiness += amount

  def decreaseHealth(self, amount):
   self.happiness -= amount

  def increaseMoney(self, amount):
   self.money += amount

  def decreaseMoney(self, amount):
   self.money -= amount

  def getHealth(self):
   return self.happiness

  def getMoney(self):
   return self.money
