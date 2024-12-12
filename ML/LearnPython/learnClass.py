class Person:
    #All classes have a function called __init__()
    #   which is always executed when the class is being initiated.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    #The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f'Person({self.name}, {self.age})'
    
p1 = Person('Nhan', 18)
p1.say_hello()

#Delete Object Properties
del p1

#Modify Object Properties
p2 = Person('Nhan', 18)
p2.age = 19
p2.name = 'Thuong'

print(p2)
