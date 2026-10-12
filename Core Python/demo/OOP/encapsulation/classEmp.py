class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name 
        self.sal = sal
        
    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid
        
    def getName(self):
        return self.name
    def setName(self, newid):
        self.name = newid
        
    def getSal(self):
        return self.sal
    def setSal(self, newid):
        self.sal = newid
        
    def display(self):
        print(f'Id:{self.id}\tName:{self.name}\tSalary:{self.sal}')
        
    def __del__(self):
        self.id = None
    
e1 = Employee(10, 'Sachin', 12345)
e2 = Employee(18, 'Virat', 6789)
print(e1.getName())
e1.display()
e2.display()
e2.setSal(1234)
e2.display()