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
        if (self.inv[0] == 0 and self.inv[1] == 0) or (self.inv[1] == 0 and self.inv[2] == 0) or (self.inv[0] == 0 and self.inv[2] == 0):
            print("No resources to recruit any armies.\n")
            return True

        return False

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
        if soldier == "S":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[1] -= 1
                return True
            
        if soldier == "A":
            if self.inv[0] -1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[2] -= 1
                return True

        if soldier == "K":
            if self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[1] -= 1
                self.inv[2] -= 1
                return True

        if soldier == "T":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                self.inv[0] -= 1
                self.inv[1] -= 1
                self.inv[2] -= 1
                return True

    def recruitFundsCheck(self,soldier):
        if soldier == "S":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0:
                return True
            else:
                return False
            
        if soldier == "A":
            if self.inv[0] -1 >= 0 and self.inv[2] - 1 >= 0:
                return True
            else:
                return False

        if soldier == "K":
            if self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                return True
            else:
                return False

        if soldier == "T":
            if self.inv[0] - 1 >= 0 and self.inv[1] - 1 >= 0 and self.inv[2] - 1 >= 0:
                return True
            else:
                return False

    def recruit(self):
        print("+++Player {}'s Stage: Recruit Armies+++".format(self.num))

        while True:
            
            print("\n[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.inv[0],self.inv[1],self.inv[2]))

            if not self.checkRecruitValid(): # CHANGE THIS TO INVERSE
                while True:
                    userRecruitName = ""
                    userRecruit = input("\nWhich type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")

                    # Alternative options
                    if userRecruit == "DIS":
                        self.game.printGameState()
                        continue
                    elif userRecruit == "PRIS":
                        self.game.pris()
                        continue
                    elif userRecruit == "QUIT":
                        self.game.quit()
                    elif userRecruit == "NO":
                        break

                    

                    # Set soldier name
                    if userRecruit == "S":
                        userRecruitName = "Spearman"                        
                    elif userRecruit == "A":
                        userRecruitName = "Archer"                      
                    elif userRecruit == "K":
                        userRecruitName = "Knight"                       
                    elif userRecruit == "T":
                        userRecruitName = "Scout"
                    else:
                        print("Sorry, invalid input. Try again.")
                        continue

                    if not self.recruitFundsCheck(userRecruit):
                        print("Insufficient resources. Try again.")
                        continue

                    break

                if userRecruit == "NO":
                    break

                while True:
                    userRecruitPosition = input("\nYou want to recruit a {}. Enter two integers as format ‘x y’ to place your army.\n".format(userRecruitName))
                    
                    # Alternative options
                    if userRecruitPosition == "DIS":
                        self.game.printGameState()
                        continue
                    if userRecruitPosition == "PRIS":
                        self.game.pris()
                        continue
                    if userRecruitPosition == "QUIT":
                        self.game.quit()

                    # Checks if input are numbers
                    if len(userRecruitPosition) != 3:
                        print("Sorry, invalid input. Try again.")
                        continue
                    if not userRecruitPosition[0].isdigit() and userRecruitPosition[2].isdigit:
                        print("Sorry, invalid input. Try again.")
                        continue # CHECK HERE, MIGHT CAUSE ERRORS
                
                    pos = (int(userRecruitPosition[0]),int(userRecruitPosition[2]))

                    # Checks if input is next to home base and if position is already taken
                    if not self.checkHomeSurrounds(pos) or self.game.board[pos[0]][pos[1]] != "  ":
                        print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                        continue

                    # Applies recruit and cost calculation
                    if self.recruitFunds(userRecruit):
                        print("\nYou has recruited a {}.".format(userRecruitName))
                        self.game.setRecruit(pos,userRecruit,self.num)

                        soldier = ""
                        if userRecruit == "S":
                            soldier = "S{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "A":
                            soldier = "A{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "K":
                            soldier = "K{}".format(self.num)
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        if userRecruit == "T":
                            soldier = "T{}".format(self.num)   
                            self.army.append(soldier)
                            self.armyPos.append(pos)
                        break
            else:
                break

    def playerArmyList(self,armyMove):
        n = self.num
        spearman = "  Spearman: "
        archer = "  Archer: "
        knight = "  Knight: "
        scout = "  Scout: "
        index = 0

        for i in self.army:
            if i == "H{}".format(n):
                index += 1
            elif i == "S{}".format(n):
                if armyMove[index] > 0:
                    spearman += "({}, {}),".format(self.armyPos[index][0],self.armyPos[index][1])
                    index += 1
            elif i == "A{}".format(n):
                if armyMove[index] > 0:
                    archer += "({}, {}),".format(self.armyPos[index][0],self.armyPos[index][1])
                    index += 1
            elif i == "K{}".format(n):
                if armyMove[index] > 0:
                    knight += "({}, {}),".format(self.armyPos[index][0],self.armyPos[index][1])
                    index += 1
            elif i == "T{}".format(n):
                if armyMove[index] > 0:
                    scout += "({}, {}),".format(self.armyPos[index][0],self.armyPos[index][1])
                    index += 1

        sum = 0
        for i in armyMove:
            sum += i
        sum -= 1

        if sum == 0:
            return False

        print("Armies to Move:")
        if spearman != "  Spearman: ":
            print(spearman[:-1])
        if archer != "  Archer: ":
            print(archer[:-1])
        if knight != "  Knight: ":
            print(knight[:-1])
        if scout != "  Scout: ":
            print(scout[:-1])
        return True

    def moveResults(self,cords,year,armyMove,enemyPlayer):

        def delEnemyIndex(enemyPlayer,dx,dy):
            enemyIndex = 0
            for i in enemyPlayer.armyPos:
                if i[0] == dx and i[1] == dy:
                    break
                else:
                    enemyIndex += 1
            del enemyPlayer.army[enemyIndex]
            del enemyPlayer.armyPos[enemyIndex]


        def challenge(soldier,indexPos,o,d,enemyPlayer):
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
                    delEnemyIndex(enemyPlayer,dx,dy)
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
                    delEnemyIndex(enemyPlayer,dx,dy)
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
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("Great! We defeated the enemy Knight!\n")
                if soldier[0] == "K":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    delEnemyIndex(enemyPlayer,dx,dy)
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
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("Great! We defeated the enemy Archer!\n")
                if soldier[0] == "A":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    delEnemyIndex(enemyPlayer,dx,dy)
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
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "K":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "A":
                    self.game.board[dx][dy] = self.army[indexPos]
                    self.game.board[ox][oy] = "  "
                    self.armyPos[indexPos] = d
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("Great! We defeated the enemy Scout!\n")
                if soldier[0] == "T":
                    self.game.board[dx][dy] = "  "
                    self.game.board[ox][oy] = "  "
                    del self.army[indexPos]
                    del self.armyPos[indexPos]
                    delEnemyIndex(enemyPlayer,dx,dy)
                    print("We destroyed the enemy Scout with massive loss!\n")

        def gameWin(soldierName):
            print("The armys {} captured the enemy's capital.\n".format(soldierName))
            name = input("What's your name, commander? ")
            print("\n***Congratulations! Emperor {} unified the country in {}.***".format(name,year))
            quit()
            
        def movePos(self,o,d,indexPos,soldier,soldierName):
            # Set destination coordinates
            ox = int(o[0])
            oy = int(o[1])
            dx = int(d[0])
            dy = int(d[1])

            if self.game.board[dx][dy] == "  ":
                self.game.board[dx][dy] = self.army[indexPos]
                self.game.board[ox][oy] = "  "
                self.armyPos[indexPos] = d
            elif self.game.board[dx][dy] == "~~":
                self.game.board[ox][oy] = "  "
                del self.armyPos[indexPos]
                del self.army[indexPos]
                print("We lost the army {} due to your command!".format(soldierName))
            elif self.game.board[dx][dy] == "WW":
                self.inv[0] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("Good. We collected 2 Wood.")
            elif self.game.board[dx][dy] == "FF":
                self.inv[1] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("Good. We collected 2 Food.")
            elif self.game.board[dx][dy] == "GG":
                self.inv[2] += 2
                self.game.board[ox][oy] = "  "
                self.game.board[dx][dy] = self.army[indexPos]
                self.armyPos[indexPos] = d
                print("Good. We collected 2 Gold.")
            elif self.game.board[dx][dy][0:1] == "H" and  self.game.board[dx][dy] != f"H{self.num}":
                gameWin(soldierName)
            elif self.game.board[dx][dy][1:2] != self.num:
                challenge(soldier,indexPos,o,d,enemyPlayer)

        # Set coordinates
        origin = (int(cords[0]),int(cords[2]))
        destination = (int(cords[4]),int(cords[6]))

        # Validity checks
        if origin == destination:
            return False
        if self.game.height < int(destination[0]) < 0:
            return False
        if self.game.width < int(destination[1]) < 0:
            return False
        for pos in self.armyPos:
            if destination == pos:
                return False
        if (abs(origin[0]-destination[0]) > 0 ) and (abs(origin[1]-destination[1]) > 0 ) :
            return False

        # Get index value of soldier player wants to move
        index = 0
        indexPos = 0

        for i in self.armyPos:
            if i == origin:
                indexPos = index
            index += 1
        soldier = self.army[indexPos]

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
        
        # Call respective move function for specific soldier type
        if soldier[0] == "T":
            if origin[0] != destination[0]: # Means moving on X axis
                if (origin[0] - destination[0] != 1) and (origin[0] - destination[0] != -1) and (origin[0] - destination[0] != -2) and (origin[0] - destination[0] != 2):
                    return False # Neither one or two steps
                else:
                    print("\nYou have moved {} from ({}, {}) to ({}, {}).".format(soldierName,origin[0],origin[1],destination[0],destination[1]))
                    armyMove[indexPos] -= 1
                    if origin[0] - destination[0] == 2: # Moving left two steps
                        firstStep = (destination[0] + 1,destination[1])
                        movePos(self,origin,firstStep,indexPos,soldier,soldierName)
                        origin = firstStep
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True
                    elif origin[0] - destination[0] == -2:
                        firstStep = (destination[0] - 1,destination[1])
                        movePos(self,origin,firstStep,indexPos,soldier,soldierName)
                        origin = firstStep
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True
                    else:
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True                 
            else: # Moving on Y axis
                if (origin[1] - destination[1] != 1) and (origin[1] - destination[1] != -1) and (origin[1] - destination[1] != -2) and (origin[1] - destination[1] != 2):
                    return False
                else:
                    print("\nYou have moved {} from ({}, {}) to ({}, {}).".format(soldierName,origin[0],origin[1],destination[0],destination[1]))
                    armyMove[indexPos] -= 1
                    if origin[1] - destination[1] == 2: # Moving left two steps
                        firstStep = (destination[0],destination[1] + 1)
                        movePos(self,origin,firstStep,indexPos,soldier,soldierName)
                        origin = firstStep
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True
                    elif origin[1] - destination[1] == -2:
                        firstStep = (destination[0],destination[1]-1)
                        movePos(self,origin,firstStep,indexPos,soldier,soldierName)
                        origin = firstStep
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True
                    else:
                        movePos(self,origin,destination,indexPos,soldier,soldierName)
                        return True  
            
        else:
            if origin[0] != destination[0]:
                if (origin[0] - destination[0] != 1) and (origin[0] - destination[0] != -1):
                    return False
            else:
                if (origin[1] - destination[1] != 1) and (origin[1] - destination[1] != -1):
                    return False
            print("\nYou have moved {} from ({}, {}) to ({}, {}).".format(soldierName,origin[0],origin[1],destination[0],destination[1]))
            movePos(self,origin,destination,indexPos,soldier,soldierName)
            armyMove[indexPos] -= 1
            return True

    def move(self,year,playerList):
        print("===Player {}'s Stage: Move Armies===\n".format(self.num))

        # Setting enemy player
        if self.num == playerList[0].num:
            enemyPlayer = playerList[1]
        else:
            enemyPlayer = playerList[0]

        armyMove = []
        for i in self.army:         
            armyMove.append(1)

        while True:
            invalidResponse = "Invalid move. Try again.\n"

            if len(self.army) == 1:
                print("\nNo Army to Move: next turn.\n")
                break
            else:
                if not self.playerArmyList(armyMove):
                    break

            cords = input("\nEnter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.\n")
            
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
            if len(cords) != 7:
                print(invalidResponse)
                continue

            if not (cords[:1].isdigit and cords[2:3].isdigit and cords[4:5].isdigit and cords[6:].isdigit):
                print(invalidResponse)
                continue
            if self.moveResults(cords,year,armyMove,enemyPlayer):
                print("meant to be here?")
                continue
            else:
                print(invalidResponse)
                continue
            

            


        



