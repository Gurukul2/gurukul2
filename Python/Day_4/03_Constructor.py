# _ _init_ _ Function

# All classes have a function called __init__(), which is always executed when the Class (Object) is being initiated.

class Student:
    name = "karan"

    def __init__(self) :
        print ("adding new student in Database...")

sl = Student()

#####--------------------------------------------------------------------------------####


#creating class
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print ("adding new student in Database...")

#creating object
s1 = Student( "Mukesh Kumar" )
print( s1.name )


# *The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the Class


class Student:
#default constructors
    def __init__ (self):
        pass

#parameterized constructors
def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print ("adding new student in Database...")


s1 = Student ("karan",97)
print(s1.name,s1.marks) #karan

s2 = Student("arjun",88)
print(s2.name,s2.marks) # arjun