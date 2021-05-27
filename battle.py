import sys

class Battle:
    def __init__(self,width, height):
        self.board = []
        for row in range(height):
            list = []
            for column in range(width):
                list.append("  ")
            self.board.append(list)
        print("Game Started: Little Battle! (enter QUIT to quit the game)")

    def setResources(self,list,resource):
        for i in list:
            if resource == "water":
                self.board[i[0]][i[1]] = "~~" 
            if resource == "food":
                self.board[i[0]][i[1]] = "FF" 
            if resource == "gold":
                self.board[i[0]][i[1]] = "GG" 
            if resource == "wood":
                self.board[i[0]][i[1]] = "WW" 
        
    def setPos(self,cords,name):
        x = cords[0]
        y = cords[1]

        self.board[x][y] = name

    def setRecruit(self,cords,name,num):
        x = cords[0]
        y = cords[1]
        input = ""

        if name == "s":
            input = "S{}".format(num)
        if name == "a":
            input = "A{}".format(num)
        if name == "k":
            input = "K{}".format(num)
        if name == "t":
            input = "T{}".format(num)    
        self.board[x][y] = input



    def printGameState(self,width,height):
        print("\nPlease check the battlefield, commander.")
        
        # Print top line
        map = "  X"
        for i in range(width):
            map += "0{} ".format(i)
        map = map[:-1]
        map += "X\n"

        # Print Y line
        map += " Y+"
        for i in range(width):
            map += "---"
        map = map[:-1]
        map += "+\n"

        # Print each row
        for i in range(height):
            map += "0{}".format(i)
            for j in range(width):
                map += "|{}".format(self.board[j][i])
            map += "|\n"

        # Print bottom Y line    
        map += " Y+"
        for i in range(width):
            map += "---"
        map = map[:-1]
        map += "+"

        print(map)

    def move(self):
        pass

    def check_finished(self):
        pass






