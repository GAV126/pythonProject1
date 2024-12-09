def pet(type, name):
    print(f"I have a {type}, and its name is {name}")

pet("cat","Solari")

#default value
def pet(type, name="kiki"):
    print(f"I have a {type}, and its name is {name}")

pet("cat" )

#Return
#用Return实际上就是在函数里没有定义print

def get_formated_name(first_name, last_name,middle_name =''):
    full_name = f"{first_name} {middle_name} {last_name}"
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

boy = get_formated_name("Gavin","yao","PengRui")
print(boy)
print("------------------------------------------------------------------------")

#下面函数返回一个字典. use variables in the function to form a dict
def build_person(first_name, last_name):
    person = {"first":first_name,"last":last_name}
    return person

doctor = build_person("Sabai","Niang")
print(doctor)

print("------------------------------------------------------------------------")

# 增加age,作为可选
def build_person(first,last, age=None):
    person={"first":first,"last":last,"age":age}
    person1={"first":first,"last":last}
    if age:
        return person
    else:
        return person1

teacher = build_person("Ming","Li" )
print(teacher)
print("------------------------------------------------------------------------")

#use while and function
def get_formated_name(first_name, last_name ):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
   f_name =input("Please enter your first name:")
   l_name = input("Please enter your last name:")
   break

yyy = (get_formated_name(f_name,l_name)).title()
print(f"welcome {yyy}")
print("------------------------------------------------------------------------")

# transfer list - variable is a list
def sayhello(names):
    for name in names:
        print(f"Hello, {name.title()}")

sayhello(["kai","julie"])



