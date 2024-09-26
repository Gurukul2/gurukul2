#Static Method Example
class Student:
   
    @staticmethod
    def collage():
        print("Welcome to Gurukul")
    

    def student_details(self, name, project):
        self.name = name
        self.project = project
        print(f"{self.name} is from the {self.project} project")

    def course_status(self, status):
        self.status = status
        print(f"{self.name} completed {self.status}% of the course")


# Example usage
s1 = Student()
s1.collage()  # Calling static method collage
s1.student_details("Abhi", "TMO")
s1.course_status(50)
