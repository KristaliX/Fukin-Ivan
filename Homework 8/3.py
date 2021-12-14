class Human:
    def __init__(self, name, brain, heart):
        self.name = name
        self.brain = brain
        self.heart = heart

    def mind(self):
        print(f'{self.name} can think')

class Student(Human):
    def __init__(self, name, brain, heart, homework):
        super().__init__(name, brain, heart)
        self.homework = int(homework)
    
    def yeswork(self):
        print(f'{self.name} сдал {self.homework} домашних заданий')
    
    def __eq__(self, other):
        return self.homework == other.homework
    
    def __ne__(self, other):
        return self.homework != other.homework

    def __lt__(self, other):
        return self.homework < other.homework

    def __gt__(self, other):
        return self.homework > other.homework

    def __le__(self, other):
        return self.homework <= other.homework

    def __ge__(self, other):
        return self.homework >= other.homework

Vasya = Student('Вася', 'Brain', 'Heart', '10')
Petr = Student('Пётр', 'Brain', 'Heart', '4')

print(f'Вася сдал больше дз чем Пётр = {Vasya.homework > Petr.homework}')
print(f'Вася сдал не меньше дз чем Пётр = {Vasya.homework >= Petr.homework}')
print(f'Вася сдал меньше дз чем Пётр = {Vasya.homework < Petr.homework}')
print(f'Вася сдал не больше дз чем Пётр = {Vasya.homework <= Petr.homework}')
print(f'Вася сдал столько же дз, сколько и Пётр = {Vasya.homework == Petr.homework}')
print(f'Вася сдал не столько же дз, сколько и Пётр = {Vasya.homework != Petr.homework}')