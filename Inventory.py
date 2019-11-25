class Inventory:
    owner = ""
    itemList = []

    def __init__(self, owner):
        self.owner = owner

    def addItem(self, item):
        self.itemList.append(item)

    def removeItem(self, item):
        self.itemList.remove(item)

    def showInventory(self):
        return self.itemList