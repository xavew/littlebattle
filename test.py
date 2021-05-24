height = 5
width = 5

board = []
for row in range(height):
    list = []
    for column in range(width):
        list.append("  ")
    board.append(list)

def setResources(list,resource):
    for i in list:
        x=1
        y=2
        z=i
        if resource == "water":
            board[i[0]][i[1]] = "~~" 

waters = [(0,0),(2,3),(4,2)]
setResources(waters,"water")

print(board)

# getting a list of coordinates
# set those coordinates in main board
# [(0,0),(4,2),(6,3)]

#def setResources(list,resource):
 #   for i in list:
 #       if resource == "water":
  #       board[i[0]][i[1]] = "~~" 