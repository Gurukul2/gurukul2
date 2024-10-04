# # Parent Class
# class Person(object):

#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     def display(self):
#         print(self.name)
#         print(self.idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
    
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post

#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))

# # creation of an object variable or an instance
# emp = Employee('Sourav', 234, 50000, "CEO")

# emp.display()
# emp.details()


# class Car:

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class MarutiCar(Car):
#         def __init__(self, brand):
#              self.brand = brand

# class Vistara(MarutiCar):
#      def __init__(self, type):
#              self.type = type

# car1 = Vistara("Electric")

# car1.start()

class A:
    varA= "welcome to class A"

class B:
    varB = "welcome to class B"

class C (A,B):
    varC = "welcome to class C"

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)