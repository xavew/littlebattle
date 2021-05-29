import sys

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

    def checkSurrounds(self,cords):
        x = cords[0]
        y = cords[1]
        if self.game.board[x+1][y] != "  " and self.game.board[x-1][y] != "  " and self.game.board[x][y+1] != "  " and self.game.board[x][y-1] != "  ":
            return True
        else:
            return False

    def checkRecruitValid(self):
        # Check map valid
        home = self.armyPos[0]
        if self.checkSurrounds(home) == True:
            print("No place to recruit new armies.")
            return True

        # # Check resources valid
        # if (self.inv[0] != 0 and self.inv[1] != 0) or (self.inv[1] != 0 and self.inv[2] != 0) or (self.inv[0] != 0 and self.inv[2] != 0):
        #     print("No resources to recruit armies.")
        #     return True

        # return False

    def checkHomeSurrounds(self,cords):
        above = list(self.armyPos[0])
        above[1] = above[1]-1
        above = tuple(above)
        below = list(self.armyPos[0])
        below[1] = below[1]+1
        below = tuple(below)
        left = list(self.armyPos[0])
        left[0] = left[0]-1
        left = tuple(left)
        right = list(self.armyPos[0])
        right[0] = right[0]+1
        right = tuple(right)

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

        while True:
            
            print("\n[Your Asset: Wood - x{} Food - x{} Gold - x{}]".format(self.inv[0],self.inv[1],self.inv[2]))

            if not self.checkRecruitValid(): # CHANGE THIS TO INVERSE
                userRecruitName = ""
                userRecruit = input("\nWhich type of army to recruit, (enter) 'S','A','K', or 'T'? Enter 'NO' to end this stage. ")
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
                elif userRecruit == "dis":
                    self.game.printGameState()
                    continue
                elif userRecruit == "pris":
                    self.game.pris()
                    continue
                elif userRecruit == "quit":
                    self.game.quit()
                    continue
                if userRecruit == "no":
                    break

                while True:
                    userRecruitPosition = input("\nYou want to recruit a {}. Enter two integers as format ‘x y’ to place your army. ".format(userRecruitName))

                    # Checks if input are numbers
                    if not userRecruitPosition.isdigit():
                        print("Sorry, invalid input. Try again.")
                        continue # CHECK HERE, MIGHT CAUSE ERRORS
                
                    pos = (int(userRecruitPosition[0]),int(userRecruitPosition[1]))
                    # Checks if input is next to home base and if position is already taken
                    if not self.checkHomeSurrounds(pos) or self.game.board[pos[0]][pos[1]] != "  ":
                        print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                        continue

                    # Applies recruit and cost calculation
                    if not self.recruitFunds(userRecruit):
                        print("Insufficient resources. Try again.")
                    else:
                        print("You has recruited a {}\n".format(userRecruitName))
                        self.game.setRecruit(pos,userRecruit,self.num)

                        soldier = ""
                        if userRecruit == "s":
                            soldier = "S{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "a":
                            soldier = "A{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "k":
                            soldier = "K{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "t":
                            soldier = "T{}".format(self.num)   
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        break
            break

    def playerArmyList(self):
        
        def formatting(cords):
            return ("(x{},y{})".format(cords[0],cords[1]))

        n = self.num
        spearman = "Spearman: "
        archer = "Archer: "
        knight = "Knight: "
        scout = "Scout: "
        index = 0

        for i in self.army:
            if i == "H{}".format(n):
                index += 1
                continue
            elif i == "S{}".format(n):
                spearman += "{},".format(formatting(self.armyPos[index]))
                index += 1
            elif i == "A{}".format(n):
                archer += "{},".format(formatting(self.armyPos[index]))
                index += 1
            elif i == "K{}".format(n):
                knight += "{},".format(formatting(self.armyPos[index]))
                index += 1
            elif i == "T{}".format(n):
                scout += "{},".format(formatting(self.armyPos[index]))
                index += 1
                
        print("Armies to Move:")
        if spearman != "Spearman: ":
            print(spearman[:-1])
        if archer != "Archer: ":
            print(archer[:-1])
        if knight != "Knight: ":
            print(knight[:-1])
        if scout != "Scout: ":
            print(scout[:-1])

    def moveResults(self,cords):
        
        def challenge(self,soldier,indexPos,o,d):
            # Set destination coordinates
            ox = int(o[0])
            oy = int(o[1])
            dx = int(d[0])
            dy = int(d[1])

            enemy = self.game.board[dx][dy]

            if enemy[0] == "S":
                if soldier[0] == "S":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We destroyed the enemy Spearman with massive loss!\n")
                if soldier[0] == "K":
                    self.game.board[ox][oy] = "  "
                    del self.armyPos[indexPos]
                    del self.army[indexPos]
                    print("We lost the army Knight due to your command!\n")
                if soldier[0] == "A":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Spearman!\n")
                if soldier[0] == "T":
                    self.game.board[ox][oy] = "  "
                    del self.armyPos[indexPos]
                    del self.army[indexPos]
                    print("We lost the army Scout due to your command!\n")
            if enemy[0] == "K":
                if soldier[0] == "S":
                    self.game.board[ox][oy] = "  "
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Knight!\n")
                if soldier[0] == "K":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We destroyed the enemy Knight with massive loss!\n")
                if soldier[0] == "A":
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We lost the army Archer due to your command!\n")
                if soldier[0] == "T":
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We lost the army Scout due to your command!\n")
            if enemy[0] == "A":
                if soldier[0] == "S":
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.army[indexPos]
                    print("We lost the army Spearman due to your command!\n")
                if soldier[0] == "K":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Archer!\n")
                if soldier[0] == "A":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We destroyed the enemy Archer with massive loss!\n")
                if soldier[0] == "T":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("We lost the army Scout due to your command!\n")
            if enemy[0] == "T":
                if soldier[0] == "S":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "K":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "A":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "T":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    print("We destroyed the enemy Scout with massive loss!\n")

        def movePos(self,o,d,indexPos,soldier):
            # Set destination coordinates
            ox = int(o[0])
            oy = int(o[1])
            dx = int(d[0])
            dy = int(d[1])

            # Set players soldier name
            soldierName = ""
            if soldier[0] == "S":
                soldierName = "Spearman"
            elif soldier[0] == "A":
                soldierName = "Archer"
            elif soldier[0] == "K":
                soldierName = "Knight"
            elif soldier[0] == "T":
                soldierName = "Scout"

            print("\nYou have moved {} from (x{},y{}) to (x{},y{}).".format(soldierName,ox,oy,dx,dy))

            if self.game.board[dx][dy] == "  ":
                self.game.board[dx][dy] = self.army[indexPos]
                self.game.board[ox][oy] = "  "
                self.armyPos[indexPos] = d
            if self.game.board[dx][dy] == "~~":
                self.game.board[ox][oy] = "  "
                del self.armyPos[indexPos]
                del self.army[indexPos]
                print("\nWe lost the army {} due to your command!".format(soldierName))
            if self.game.board[dx][dy] == "WW":
                self.inv[0] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("\nGood. We collected 2 Wood.")
            if self.game.board[dx][dy] == "FF":
                self.inv[1] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("\nGood. We collected 2 Food.")
            if self.game.board[dx][dy] == "GG":
                self.inv[2] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("\nGood. We collected 2 Gold.")
            if self.game.board[dx][dy] == "S{}".format(otherPlayer):
                challenge(soldier,indexPos,o,d)
            if self.game.board[dx][dy] == "A{}".format(otherPlayer):
                challenge(soldier,indexPos,o,d)
            if self.game.board[dx][dy] == "K{}".format(otherPlayer):
                challenge(soldier,indexPos,o,d)
            if self.game.board[dx][dy] == "T{}".format(otherPlayer):
                challenge(soldier,indexPos,o,d)

        # Set coordinates
        origin = (int(cords[1]),int(cords[4]))
        destination = (int(cords[7]),int(cords[10]))

        # Validity checks
        if origin == destination:
            print("origin is destination")
            return False
        if self.game.height < int(destination[0]) < 0:
            print("map height prob")
            return False
        if self.game.width < int(destination[1]) < 0:
            print("map width prob")
            return False
        for pos in self.armyPos:
            if destination == pos:
                print("army already there")
                return False

        # Set challengers number
        otherPlayer = 0
        if self.num == 1:
            otherPlayer = 2
        else:
            otherPlayer = 1

        # Get index value of soldier player wants to move
        index = 0
        indexPos = 0

        for i in self.armyPos:
            if i == origin:
                indexPos = index
            index += 1
        soldier = self.army[indexPos]

        # Call respective move function for specific soldier type
        if soldier == "T{}".format(self.num):
            pass
        else:
            movePos(self,origin,destination,indexPos,soldier)
            self.game.printGameState()
            return True

    def move(self):
        print("===Player {}'s Stage: Move Armies===\n".format(self.num))
        while True:
            invalidResponse = "Invalid blah\n"

            if len(self.army) == 1:
                print("No Army to Move: next turn\n")
                break
            else:
                self.playerArmyList()

            cords = input("\nEnter four integers as a format 'x0 y0 x1 y1' to represent move unit from (x0,y0) to (x1,y1) or 'NO' to end this turn. ")
            
            # Alternative options checking
            if cords == "NO":
                print()
                break
            elif cords == "DIS":
                self.game.printGameState()
                continue
            elif cords == "PRIS":
                self.game.pris()
                continue
            elif cords == "QUIT":
                self.game.quit()
            
            # Valid input checking
            if len(cords) != 11:
                print(invalidResponse)
                continue
            if not (cords[:1].isalpha and cords[1:2].isnumeric and cords[3:4].isalpha and cords[4:5].isnumeric and cords[6:7].isalpha 
            and cords[7:8].isnumeric and cords[9:10].isalpha and cords[10:].isnumeric):
                print(invalidResponse)
                continue
            if self.moveResults(cords):
                break
            else:
                print(invalidResponse)
                continue
            

            


        



