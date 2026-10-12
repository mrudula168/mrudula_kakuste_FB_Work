class Student:
    stCount = 0
    def __init__(self,frn,name,bname):
        self.frn = frn
        self.name = name
        self.batch = bname
        Student.stCount += 1
    def display(self):
        print(f'FRN:{self.frn}\tName:{self.name}\tBatch:{self.batch}\tStudent Count:{Student.stCount}')
        
class placedStudent(Student):
    def __init__(self,frn,name,bname,cname):
        super().__init__(frn,name,bname)
        self.cname = cname
    def setCname(self,cname):
        self.cname = cname
    def getCname(self):
        return self.cname
    def display(self):
        print(f'Cname:{self.cname}')
        super().dispaly()

        
s1 = Student(12,'Gaurav','April')
s2 = Student(1,'Atharva','July/Aug')
s3 = Student(53,'Rutika','July/Aug')
s4 = placedStudent(37,'Shivraj','July/Aug','TCS')
s5 = placedStudent(18,'Virat','July/Aug','One8')
print(Student.stCount)