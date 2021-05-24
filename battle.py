import sys

class Battle:
  def __init__(self,width, height):
    self.board = []
    for row in range(height):
        list = []
        for column in range(width):
            list.append("  ")
        self.board.append(list)
    
    Battle.printGameState(width, height)

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
    map += "+\n"

    print(map)

  def move(self):
    pass

  def check_finished(self):
    pass

