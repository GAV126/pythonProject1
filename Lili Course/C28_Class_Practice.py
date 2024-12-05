
class Student:
    def __init__(self, name, student_id):
    # self.name is the attribute the object has ,and the second name is a variable.
        self.name = name
        self.student_id = student_id
    # grade is not in the __init__ function
        self.grades = {"Chinese":0,"Math":0,"English":0}

# update course grade
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] =grade
        else:
            print("Wrong course")

# print all grades of courses
    def print_grades(self):
       print(f"Student {self.name} Student_id : {self.student_id}" )
       for course in self.grades:
           print(f"{course}:{self.grades[course]}")


# should be outside the class when make an object instance
chen = Student("Chen","04241")
zeng = Student("Zeng","04242")

print(zeng.name)
print(zeng.student_id)
print(zeng.grades)
zeng.set_grade("Math",95)
print(zeng.grades)  # need print

print("-------------------------------------------")

chen.set_grade("Chinese",92)
chen.set_grade("Math",88)
chen.set_grade("English",99)
chen.print_grades()




