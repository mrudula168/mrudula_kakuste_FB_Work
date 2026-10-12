class College:
    def __init__(self, collegeid, name, fees):
        self.collegeid = collegeid
        self.name = name
        self.fees = fees
    
    def getCollegeid(self):
        return self.collegeid
    def setCollegeid(self, newid):
        self.collegeid = newid
        
    def getName(self):
        return self.name
    def setName(self, newid):
        self.name = newid
        
    def getFees(self):
        return self.fees
    def setFees(self, newid):
        self.fees = newid
        
    def display(self):
        print(f'Collegeid:{self.collegeid}\tName:{self.name}\tFees:{self.fees}')
        
c1 = College(1, 'Adypsoe', 11000)
c2 = College(2, 'Mmcoe', 21000)
c1.display()
c2.display()