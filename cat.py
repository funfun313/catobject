class Cat:
    name = ""
    color = ""
    favoritetoy = ""
    def __init__(self,name):
        self.name = name
    def purr(self):
        print("Meow! My name is " + self.name) 

fluffy = Cat("Fluffy")
snowball = Cat("Snowball")
