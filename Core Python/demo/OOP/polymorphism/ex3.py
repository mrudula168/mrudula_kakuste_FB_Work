class Crop:
    def __init__(self, name, season, area, price):
        self.name = name
        self.season = season
        self.area = area
        self.price = price
        
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
        
    def Calprice(self):
        print(f'Total price:{self.price}') 
        
    def display(self):
        print(f'CropName:{self.name}\tSeason:{self.season}\tArea:{self.area}acre')
        
#Crop class ends here.....................

class Fruit(Crop):
    def __init__(self, name, season, area, price, sweetness):
        super().__init__(name, season, area, price)
        self.sweetness = sweetness
    def getSweetness(self):
        return self.sweetness
    def setSweetness(self, newid):
        self.sweetness = newid
    def Calprice(self):
        print(f'Total price:{self.price*self.sweetness}') 
    def display(self):
        print(f'Sweetness:{self.sweetness}%\t')
        return super().display()

# Fruitclass ends here..............

class Grains(Crop):
    def __init__(self, name, season, area, price, weight):
        super().__init__(name, season, area, price)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def setWeight(self, newid):
        self.weight = newid
    def Calprice(self):
            print(f'Total price:{self.price*self.weight}') 
    def display(self):
        print(f'Weight:{self.weight}kg\t')
        return super().display()
    
#Grains class ends here..............

c1 = Crop('Onion', 'Rainy', 3, 60)
f1 = Fruit('Pomogrenate', 'summer', 12, 80, 3)
g1 = Grains('wheat', 'Winter', 10, 50, 2)

c1.Calprice()
f1.Calprice()
g1.Calprice()