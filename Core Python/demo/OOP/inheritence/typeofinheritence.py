# multilevel inheritence
# class Emp:
#     print('Employee')
# class scalesManager(Emp):
#     def __init__(self):
#         super().__init__()
#         print('Scalesmanager')
# class AreaSM(scalesManager):
#     def __init__(self):
#         super().__init__()
#         print('AreaSM')
        
# a = AreaSM()

# Herirchical inheritence
# class Player:
#     def __init__(self, name, jrno):
#         self.name = name
#         self.jrno = jrno
#     def display(self):
#         print(f'Name:{self.name}\tJrno:{self.jrno}')
# class CricketP(Player):
#     def __init__(self, name, jrno, runs):
#         super().__init__(name, jrno)
#         self.runs = runs
#     def display(self):
#         print(f'runs:{self.runs}')
#         return super().display()
# class kabbadiP(Player):
#     def __init__(self, name, jrno, raidp):
#         super().__init__(name, jrno)
#         self.raidp = raidp
#     def display(self):
#         print(f'raidp:{self.raidp}')
#         return super().display()

# p1 = Player('Swaraj', 3)
# p2 = CricketP('Virat', 18 , 100)
# p3 = kabbadiP('Paradeep', 7, 12)
# p1.display()
# p2.display()
# p3.display()

# multiple inheritence

class Electrical:
    def display(self):
        print('Electrical')
        
class Mechanical:
    def display(self):
        print('Mechanical')
        
class Mechatronix(Electrical, Mechanical):
    # def display(self):
    #     print('Mechatronix')
    pass
m = Mechatronix()
m.display()