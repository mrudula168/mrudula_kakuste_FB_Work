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
    
    def CalSal(self):
        print(f'Final salary of employee:{self.sal}')
    
    def __str__(self):
        return f'Id:{self.id}\tName:{self.name}\tSalary:{self.sal}'
    
    def display(self):
        print(f'Id:{self.id}\tName:{self.name}\tSalary:{self.sal}')
        
#Emp class ends here......................

class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com = com
    def getCom(self):
        return self.com
    def setCom(self, newid):
        self.com = newid
    def CalSal(self):
        print(f'Final salary of HR:{self.com + self.sal}')
    def __str__(self):
        return super().__str__()+f'\tCom:{self.com}'
    def display(self):
        print(f'Com:{self.com}\t')
        return super().display()
    
#Hrclass ends here...................

class Devloper(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus
    def getBonus(self):
        return self.Bonus
    def setBonus(self, newid):
        self.Bonus = newid
    def CalSal(self):
        print(f'Final salary of Devloper:{self.bonus + self.sal}')
    def __str__(self):
        return super().__str__()+f'\tBonus:{self.bonus}'
    def display(self):
        print(f'Bonus:{self.bonus}\t')
        return super().display()
        
#Devloper class ends here.........................
    
e1 = Employee(1, 'Rahul', 12345)
h1 = Hr(7, 'Harman', 6789, 1500)
d1 = Devloper(63, 'Surya', 8956, 789)

print(e1)
print(h1)
print(d1)