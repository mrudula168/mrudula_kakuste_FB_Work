class Student:
    
    iname = 'fbs'
    @staticmethod
    def setIname(niname):
        Student.iname = niname
        
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname
        
    def getFrn(self):
        return self.frn
    def setFrn(self, newid):
        self.frn = newid
        
    def getName(self):
        return self.name
    def setName(self, newid):
        self.name = newid
        
    def getBatch(self):
        return self.bname
    def setBatch(self, newid):
        self.bname = newid
    
    def display(self):
        print(f'Frn:{self.frn} \tName:{self.name} \tBatch:{self.bname} \tInstitute:{Student.iname}')
        
s1 = Student(12, 'Gaurav', '17 April')
s2 = Student(22, 'Suraj', 'Aug')
s3 = Student(17, 'Pramod', 'july/aug')
s1.display()
s2.display()
s3.display()
print(Student.iname)
Student.setIname('Fistbit Solutions')
print(Student.iname)
