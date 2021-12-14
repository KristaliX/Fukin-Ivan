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
        self.homework = homework
    
    def yeswork(self):
        print(f'{self.name} сдал {self.homework} домашних заданий')

Vasya = Student('Вася', 'Brain', 'Heart', '10')
Petr = Student('Пётр', 'Brain', 'Heart', '5')

Vasya.yeswork()
Petr.yeswork()