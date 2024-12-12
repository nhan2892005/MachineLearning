class Animals:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f'It is {self.name}.'

class Herbivore(Animals):
    def __init__(self, name, age, gender, food):
        super().__init__(name, age, gender)
        self.food = food

    def get_food(self):
        return f'The {self.name} eat {self.food}'

A1 = Herbivore('Lion', 5, 'male', 'Rabbit')

print(A1.get_food())

    