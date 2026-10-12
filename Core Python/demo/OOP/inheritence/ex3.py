class Crop:
    def __init__(self, name, season, area):
        self.name = name
        self.season = season
        self.area = area
        
    def getName(self):
        return self.name
    def setName(self,newid):
        self.name = newid
        
    def getSeason(self):
        return self.season
    def setSeason(self, newid):
        self.season = newid
        
    def getArea(self):
        return self.area
    def setArea(self, newid):
        self.area = newid
        
    def display(self):
        print(f'CropName:{self.name}\tSeason:{self.season}\tArea:{self.area}acre')
        
#Crop class ends here.....................

class Fruit(Crop):
    def __init__(self, name, season, area, sweetness):
        super().__init__(name, season, area)
        self.sweetness = sweetness
    def getSweetness(self):
        return self.sweetness
    def setSweetness(self, newid):
        self.sweetness = newid
    def display(self):
        print(f'Sweetness:{self.sweetness}%\t')
        return super().display()

# Fruitclass ends here..............

class Grains(Crop):
    def __init__(self, name, season, area, weight):
        super().__init__(name, season, area)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def setWeight(self, newid):
        self.weight = newid
    def display(self):
        print(f'Weight:{self.weight}kg\t')
        return super().display()
    
#Grains class ends here..............

c1 = Crop('Onion', 'Rainy', 3)
f1 = Fruit('Pomogrenate', 'summer', 12, 80)
g1 = Grains('wheat', 'Winter', 10, 12)

c1.display()
f1.display()
g1.display()