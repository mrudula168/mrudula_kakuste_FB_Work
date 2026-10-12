class Examination:
    def __init__(self, examid, subject, date):
        self.examid = examid
        self.subject = subject
        self.date = date
        
    def getExamid(self):
        return self.examid
    def setExamid(self,newid):
        self.examid = newid
        
    def getSubject(self):
        return self.subject
    def setSubject(self,newid):
        self.subject = newid
        
    def getDate(self):
        return self.date
    def setDate(self,newid):
        self.date = newid
        
    def display(self):
        print(f'Examid:{self.examid}\tSubject:{self.subject}\tDate:{self.date}')
        
# Examination class ends here.....................

class Writtenexam(Examination):
    def __init__(self, examid, subject, date, units):
        super().__init__(examid, subject, date)
        self.units = units
    def getUnits(self):
        return self.units
    def setUnits(self, newid):
        self.units = newid
    def display(self):
        print(f'Units:{self.units}')
        return super().display()
    
#Writtenexam class ends here.....................

class Practicalexam(Examination):
    def __init__(self, examid, subject, date, expno):
        super().__init__(examid, subject, date)
        self.expno = expno
    def getExpno(self):
        return self.expno
    def setExpno(self,newid):
        self.expno = newid
    def display(self):
        print(f'Expno:{self.expno}')
        return super().display()
    
#Practical exam class ends here....................

e1 = Examination(1, 'Math', '12-9')
w1 = Writtenexam(2, 'English', '13-9', 5)
p1 = Practicalexam(3, 'Chemistry', '14-9', 3)

e1.display()
w1.display()
p1.display()