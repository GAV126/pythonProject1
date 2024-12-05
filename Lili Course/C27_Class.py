class CuteCat:
    def __init__(self):
        self.name = "Boston"

Cat1=CuteCat()
print(Cat1.name)

#
class CuteCat:
    def __init__(self, cat_name):
        self.name = cat_name

Cat1=CuteCat("Jojo")
print(Cat1.name)

#
class CuteCat:
    def __init__(self, cat_name,cat_age,cat_colour):
        self.cat_age = cat_age
        self.cat_name = cat_name
        self.cat_colour = cat_colour


cat1=CuteCat("Jojo",1,"White")
print(f"{cat1.cat_name} 's age is {cat1.cat_age} and colour is {cat1.cat_colour} ")

#methond
class CuteCat:
    def __init__(self, cat_name,cat_age,cat_colour):
        self.age = cat_age
        self.name = cat_name
        self.colour = cat_colour

    def speak(self):
        print("M" * self.age)
    def think(self,content):
        print(f"cat {self.name} is thinking {content}")
cat1= CuteCat("momo",2,"Org")
cat1.speak()
cat1.think("Go to park or stay at home?")