class Item:
    itemName = ""
    count = 0
    slogan = ""
    weight = 0.0

    localItem = {"name": itemName, "count": count, "slogan": slogan, "weight": weight}

    def __init__(self, name, count, slogan, weight):
        self.itemName = name
        self.count = count
        self.slogan = slogan
        self.weight = weight

    def setName(self, name):
        self.itemName = name

    def getName(self, name):
        return self.name

    def addCount(self, num):
        self.count = self.count + num

    def subtractCount(self, num):
        self.count = self.count - num

    def getCount(self, newCount):
        self.count = newCount
        return self.count

    def setSlogan(self, newSlogan):
        self.slogan = newSlogan

    def getSlogan(self, newSlogan):
        self.slogan = newSlogan
        return self.slogan

    def addWeight(self, weight):
        self.weight = self.weight + weight

    def subtractWeight(self, weight):
        self.weight = self.weight - weight

    def getWeight(self):
        return self.weight
