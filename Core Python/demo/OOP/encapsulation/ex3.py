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
        print(f'CropName:{self.name}\tSeason:{self.season}\tArea:{self.area}')
        
c1 = Crop('Fruit', 'summer', 12)
c2 = Crop('Grains', 'Winter', 10)
c1.display()
c2.display()
c2.setSeason('rainy')
c2.display()