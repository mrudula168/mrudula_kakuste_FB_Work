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
        
#College class ends here................

class Engcollege(College):
    def __init__(self, collegeid, name, branch, fees):
        super().__init__(collegeid, name, fees)
        self.branch = branch
    def getBranch(self):
        return self.branch
    def setBranch(self,newid):
        self.branch = newid
    def display(self):
        print(f'Branch:{self.branch}\t')
        return super().display()
    
#engclass ends here..................

class Medicalcollege(College):
    def __init__(self, collegeid, name, specialization, fees):
        super().__init__(collegeid, name, fees)
        self.specialization = specialization
    def getSpecialization(self):
        return self.specialization
    def setSpecialization(self, newid):
        self.specialization = newid
    def display(self):
        print(f'Specialization:{self.specialization}\t')
        return super().display()
    
c1 = College(1, 'Adypsoe', 11000)
e1 = Engcollege(2, 'Mmcoe', 'DS', 21000 )
m1 = Medicalcollege(3, 'Dypmc', 'BDS', 300000)
c1.display()
e1.display()
m1.display()