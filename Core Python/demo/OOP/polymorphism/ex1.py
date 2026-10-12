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
    
    def Calfees(self):
        print(f'Total fees:{self.fees}')
        
    def display(self):
        print(f'Collegeid:{self.collegeid}\tName:{self.name}\tFees:{self.fees}')
        
#College class ends here................

class Govtcollege(College):
    def __init__(self, collegeid, name, fees, scholarship):
        super().__init__(collegeid, name, fees)
        self.scholarship = scholarship
    def getScholarship(self):
        return self.scholarship
    def setScholarship(self,newid):
        self.scholarship = newid
    def Calfees(self):
        print(f'Total fees:{self.fees+self.scholarship}')
    
#Govtclass ends here..................

class Privatecollege(College):
    def __init__(self, collegeid, name, fees, donation):
        super().__init__(collegeid, name, fees)
        self.donation = donation
    def getdonation(self):
        return self.donation
    def setdonation(self, newid):
        self.donation = newid
    def Calfees(self):
            print(f'Total fees:{self.fees+self.donation}')
    
c1 = College(1, 'Adypsoe', 11000)
g1 = Govtcollege(2, 'Mmcoe', 21000, 70000)
p1 = Privatecollege(3, 'Dypmc', 300000, 200000)
c1.Calfees()
g1.Calfees()
p1.Calfees()