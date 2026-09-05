class Student:
    college_name="Sagar College"

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

stu1=Student("Bikash",9.90)
print(stu1.name,stu1.cgpa)
print(Student.college_name)
