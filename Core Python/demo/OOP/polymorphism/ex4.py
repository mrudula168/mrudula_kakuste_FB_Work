class Examination:
    def __init__(self, examid, subject, date, marks):
        self.examid = examid
        self.subject = subject
        self.date = date
        self.marks = marks
        
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
        
    def getMarks(self):
        return self.marks
    def setMarks(self,newid):
        self.marks = newid
        
    def Calmarks(self):
        print(f'Total marks:{self.marks}')
        
    def display(self):
        print(f'Examid:{self.examid}\tSubject:{self.subject}\tDate:{self.date}')
        
# Examination class ends here.....................

class Writtenexam(Examination):
    def __init__(self, examid, subject, date, units, marks, utmarks):
        super().__init__(examid, subject, date, marks)
        self.units = units
        self.utmarks = utmarks
    def getUnits(self):
        return self.units
    def setUnits(self, newid):
        self.units = newid
    def Calmarks(self):
        print(f'Total marks:{self.marks+self.utmarks}')
    def display(self):
        print(f'Units:{self.units}')
        return super().display()
    
#Writtenexam class ends here.....................

class Practicalexam(Examination):
    def __init__(self, examid, subject, date, expno, marks, internalmarks):
        super().__init__(examid, subject, date, marks)
        self.expno = expno
        self.internalmarks = internalmarks
    def getExpno(self):
        return self.expno
    def setExpno(self,newid):
        self.expno = newid
    def Calmarks(self):
        print(f'Total marks:{self.marks+self.internalmarks}')
    def display(self):
        print(f'Expno:{self.expno}')
        return super().display()
    
#Practical exam class ends here....................

e1 = Examination(1, 'Math', '12-9', 60)
w1 = Writtenexam(2, 'English', '13-9', 5, 60, 20)
p1 = Practicalexam(3, 'Chemistry', '14-9', 3, 60, 25)

e1.Calmarks()
w1.Calmarks()
p1.Calmarks()