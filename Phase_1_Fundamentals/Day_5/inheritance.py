from chef import Chef
from chinesechef import ChineseChef

myChef = Chef()
myChef.make_special_dish() # Prints "bbq ribs"

myChineseChef = ChineseChef()
myChineseChef.make_chicken()      # Inherited from Chef
myChineseChef.make_special_dish() # Uses the Overwritten version (orange chicken)
myChineseChef.make_fried_rice()   # Only the ChineseChef can do this