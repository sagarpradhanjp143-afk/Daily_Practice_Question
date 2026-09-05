# init methode is also known as a construcot 

# to instailse the object is calleed a init 

# self is a bydefault paramete it is always fixed 

# sef is storing instacne of the class 

# class Student:
#     def __init__(self):
#         print("construcor is called ")

# stu1=Student()

class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

    def get_cgpa(self):
        return self.cgpa

stu1=Student("Sagar",8.7)
# print(stu1.name,stu1.cgpa)
print(stu1.get_cgpa())
# it is a two types of consrtuctot that is default and parametreetrsjcdeo



