import sys
from test import checkHomeSurrounds

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

        return False



    def checkHomeSurrounds(self,cords):
        above = self.armyPos[0]
        above[1] = above[1]-1
        below = self.armyPos[0]
        below[1] = below[1]+1
        left = self.armyPos[0]
        left[0] = left[0]-1
        right = self.armyPos[0]
        right[0] = right[0]+1

        if cords == above or cords == below or cords == left or cords == right:
            return True
        else:
            return False

    def recruitFunds(self,soldier):
        if soldier == "s":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[1] -= 1
                return True
            else:
                return False
            
        if soldier == "a":
            if self.inv[0] -1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[2] -= 1
                return True
            else:
                return False

        if soldier == "k":
            if self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[1] -= 1
                self.inv[2] -= 1
                return True
            else:
                return False

        if soldier == "t":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[1] -= 1
                self.inv[2] -= 1
                return True
            else:
                return False

        # There are four types of soldiers: 
        # Spearman (S) costs 1W, 1F; 
        # Archer (A) costs 1W, 1G; 
        # Knight (K) costs 1F, 1G, 
        # self.inv = [2,2,2] # Wood, Food, Gold


    def recruit(self):
        print("+++Player {}'s Stage: Recruit Armies+++".format(self.num))
        print("[Your Asset: Wood - x{} Food - x{} Gold - x{}]".format(self.inv[0],self.inv[1],self.inv[2]))

        if not self.checkRecruitValid(): # CHANGE THIS TO INVERSE
            userRecruitName = ""
            userRecruit = input("\nWhich type of army to recruit, (enter) 'S','A','K', or 'T'? Enter 'NO' to end this stage.")
            userRecruit = userRecruit.lower()

            # Set soldier name
            if userRecruit == "s":
                userRecruitName = "Spearman"
            elif userRecruit == "a":
                userRecruitName = "Archer"
            elif userRecruit == "k":
                userRecruitName = "Knight"
            elif userRecruit == "t":
                userRecruitName = "Scout"

            while userRecruit != "NO":
                while True:
                    userRecruitPosition = input("\nYou want to recruit a {}. Enter two integers as format ‘x y’ to place your army.".format(userRecruitName))

                    # Checks if input are numbers
                    if not userRecruitPosition.isdigit():
                        print("Sorry, invalid input. Try again.")
                        continue # CHECK HERE, MIGHT CAUSE ERRORS
                
                    pos = (userRecruitPosition[0],userRecruitPosition[1])
                    # Checks if input is next to home base and if position is already taken
                    if not checkHomeSurrounds(pos) or self.board[pos[0]][pos[1]] != "  ":
                        print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                        continue

                    # Applies recruit and cost calculation
                    if not self.recruitFunds(pos):
                        print("Insufficient resources. Try again.")
                    else:
                        print("You has recruited a {}\n".format(userRecruitName))






