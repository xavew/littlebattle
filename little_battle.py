import sys

# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  width, height = 0, 0
  waters, woods, foods, golds = [], [], [], [] # list of position tuples

  file = open("config.txt", "r")
  content = file.readlines()

  def checkInitialFormat():
    flag = False
    if content[0].split(" ")[0] != "Frame:":
      flag = True
    if content[1].split(" ")[0] != "Water:":
      flag = True
    if content[2].split(" ")[0] != "Wood:":
      flag = True
    if content[3].split(" ")[0] != "Food:":
      flag = True
    if content[4].split(" ")[0] != "Gold:":
      flag = True
    if flag == True:
      raise SyntaxError("Invalid Configuration File: format error!")

  def checkFrameContent():
    frameText = content[0].split(" ")[1]

    if frameText[0:1].isdigit() and frameText[1:2] == "x" and frameText[2:3].isdigit:
      if 4 < int(frameText[0:1]) < 8 and 4 < int(frameText[2:3]) < 8:
        width = frameText[0:1]
        height = frameText[2:3]
      else:
        raise ArithmeticError(" Invalid Configuration File: width and height should range from 5 to 7!")
    else:
      raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")

  # Function used to check if a resource coordinate is already in use
  def checkExists(cords):
    if cords in waters:
      return True
    elif cords in woods:
      return True
    elif cords in foods:
      return True
    elif cords in golds:
      return True
    else:
      return False

  def checkValid(cords):
    
    pass

  def setCords():
    item = waters
    itemName = "Water"
    itemIndex = 1

    while True:
      itemContent = content[itemIndex].split(": ")[1]
      itemContent = itemContent.replace(" ","")
      length = len(itemContent)-1
      index = 0

      if length % 2 != 0:
        raise SyntaxError("Invalid Configuration File: {} has an odd number of elements!".format(itemName))
      
      if itemContent.isdigit == False:
        raise ValueError("Invalid Configuration File: {} contains non integer characters!".format(itemName))

      while index < length:
        cords = (int(itemContent[index:index+1]),int(itemContent[index+1:index+2]))
        if checkExists(cords):
          raise SyntaxError("Invalid Configuration File: Duplicate position ({}, {})!".format(cords[0],cords[1]))
        item.append(cords)
        index += 2

      if item == waters:
        item = woods
        itemName = "Wood"
        itemIndex = 2
      elif item == woods:
        item = foods
        itemName = "Food"
        itemIndex = 3
      elif item == foods:
        item = golds
        itemName = "Gold"
        itemIndex = 4
      else:
        break

  checkInitialFormat()
  checkFrameContent()
  setCords()
  print("Water:")
  print(waters)
  print("Wood:")
  print(woods)
  print("Food:")
  print(foods)
  print("Gold:")
  print(golds)
  return width, height, waters, woods, foods, golds

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()
  width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])

