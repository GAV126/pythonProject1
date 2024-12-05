# Father class
class Mammal:
# NOTE: init spelling
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breathe(self):
        print(self.name + " is breathing")
    def poop(self):
        print(self.name + " is Pooping")

# human = Mammal("Kai","Male")
# human.poop()

# two children class
class Human(Mammal):
    def read(self):
        print(self.name + " is reading")

class Cat(Mammal):
    def scratch_sofa(self):
        print(self.name + " is scratching my sofa")

    def poop(self):
        print(self.name + " is Pooping in child class")

cat1 = Cat("Jojo","Male")
# Call father method Poop() if there no poop in child. Call child poop if there is a poop method in Cat class
# Check child class first, if no, go the father class
cat1.poop()