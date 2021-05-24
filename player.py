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

    def recruit(self):
        print("+++Player {}'s Stage: Recruit Armies+++".format(self.num))
        print("[Your Asset: Wood - x{} Food - x{} Gold - x{}]".format(self.inv[0],self.inv[1],self.inv[2]))
        self.checkRecruitValid()



    def checkRecruitValid(self):
        # Check map valid
        home = self.armyPos[0]
        if self.game.checkSurrounds(home) == True:
            print("No place to recruit new armies.")
            return True

        # Check resources valid
        if (self.inv[0] != 0 and self.inv[1] != 0) or (self.inv[1] != 0 and self.inv[2] != 0) or (self.inv[0] != 0 and self.inv[2] != 0):
            print("No resources to recruit armies.")
            return True


        # There are four types of soldiers: 
        # Spearman (S) costs 1W, 1F; 
        # Archer (A) costs 1W, 1G; 
        # Knight (K) costs 1F, 1G, 

        # [1,1,0]
        # [0,1,1]
        # [1,0,1]
