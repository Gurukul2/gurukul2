# Class Creation
class Student:
    collage_name = 'Gurukul'

    def __init__(self):
        print("welcome to ",self.collage_name)

    def student_details(self, name , project):
        self.name = name
        self.project = project
        print(f"{self.name} is from {self.project} project")

    def course_status(self, status):
        self.status = status
        print(f"{self.name} Completed {self.status} % of the course")


s1 = Student()
s1.student_details("Abhi","TMO")
s1.course_status(50)
