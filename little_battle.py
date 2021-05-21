import sys

# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  width, height = 0, 0
  waters, woods, foods, golds = [], [], [], [] # list of position tuples
  
  return width, height, waters, woods, foods, golds

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()
  width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])

print("test")

#newbranchtest