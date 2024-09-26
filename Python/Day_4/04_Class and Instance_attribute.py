class Student:
    college_name = "ABC College"
    name = "anonymous"  #class attr

def __init__ (self, name, marks):
    self.name = name #obj attr > class attr
    self .marks = marks
    print("adding new student in Database..")



sl = Student ("karan", 97)
print (sl. name)