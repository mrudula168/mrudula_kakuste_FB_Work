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
        
e1 = Examination(1, 'Maths', 12)
e2 = Examination(2, 'English', 13)
e1.display()
e2.display()
print(e1.getSubject())
e2.setDate(14)
e2.display()