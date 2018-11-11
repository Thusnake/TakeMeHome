class Player:
    def __init__(self):
        self.health = 100
        self.money = 1000

    def increaseHealth(self, amount):
     self.health += amount

    def decreaseHealth(self, amount):
     self.health -= amount

    def increaseMoney(self, amount):
     self.money += amount

    def decreaseMoney(self, amount):
     self.money -= amount

    def getHealth(self):
     return self.health

    def getMoney(self):
     return self.money
