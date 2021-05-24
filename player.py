import sys
from battle import Battle

class Player():
    def __init__(self,num,game):
        self.num = num
        self.game = game
        self.inv = [2,2,2] # Wood, Food, Gold
        self.army = []
        self.armyPos = []


    def setBase(self,height,width):
        self.army.append("H{}".format(self.num))

        if self.num == 1:
            self.armyPos.append((1,1))
            self.game.setPos((1,1),"H1")
        else:
            self.armyPos.append((width-2,height-2))
            self.game.setPos((width-2,height-2),"H2")
