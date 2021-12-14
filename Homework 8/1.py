class Animals:
    def __init__(self, name, move_organs, organ_system, meal):
        self.name = name
        self.move_organs = move_organs
        self.organ_system = organ_system
        self.meal = meal
        
    def move(self):
        print(f'{self.name} can movement')

    def eat(self):
        print(f'{self.name} can eat')

    def sleep(self):
        print(f'{self.name} can sleep')

class Mammals(Animals):
    def __init__(self, name, move_organs, organ_system, meal, wool, heart):
        super().__init__(name, move_organs, organ_system, meal)
        self.wool = wool
        self.heart = heart
    
    def meal(self):
        print(f'{self.name} can find meal for childs')

    def gen(self):
        print(f'{self.name} can have childs')

class Human(Mammals):
    def __init__(self, name, move_organs, organ_system, meal, wool, heart, brain):
        super().__init__(name, move_organs, organ_system, meal, wool, heart)
        self.brain = brain

    def mind(self):
        print(f'{self.name} can think')

class Cat(Mammals):
    def __init__(self, name, move_organs, organ_system, meal, wool, heart, mustache):
        super().__init__(name, move_organs, organ_system, meal, wool, heart)
        self.mustache = mustache

    def sound(self):
        print(f'{self.name} can MEOW')
    
class Dog(Mammals):
    def __init__(self, name, move_organs, organ_system, meal, wool, heart, wolf):
        super().__init__(name, move_organs, organ_system, meal, wool, heart)
        self.wolf = wolf
    
    def sound(self):
        print(f'{self.name} can WOOF')

Animal = Animals('Animal', 'Move organs', 'Organ system', 'Meal')
print(Animal.name)
print(Animal.move_organs)
Animal.eat()
Animal.move()
Animal.sleep()

John = Human('John', 'Move organs', 'Organ system', 'Meal', 'Hair', 'Heart', 'Brain' )
print('\n' + John.name)
print(John.brain)
John.eat()
John.mind()
John.gen()

Mammal = Mammals('Mammal', 'Move organs', 'Organ system', 'Meal', 'Wool', 'Heart')
print('\n' + Mammal.name)
print(Mammal.wool)
Mammal.eat()
Mammal.gen()

Ishtar = Cat('Ishtar', 'Move organs', 'Organ system', 'Meal', 'Wool', 'Heart', 'Mustache')
print('\n' + Ishtar.name)
print(Ishtar.mustache)
Ishtar.sound()

Karl = Dog('Karl', 'Move organs', 'Organ system', 'Meal', 'Wool', 'Heart', 'Half wolf')
print('\n' + Karl.name)
print(Karl.wolf)
Karl.sound()