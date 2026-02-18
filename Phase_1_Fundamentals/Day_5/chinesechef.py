from chef import Chef


# This tells Python: ChineseChef can do everything Chef can do
class ChineseChef(Chef):

    # This is a special function only the ChineseChef has
    def make_fried_rice(self):
        print("The chef makes fried rice")

    # We can also Overwrite function
    def make_special_dish(self):
        print("The chef makes orange chicken")