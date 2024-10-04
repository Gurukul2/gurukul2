class Base:
    def __init__(self):
        self.a = "Gurukul"
        self.__c = "PythonOOPSConcept"  # Private variable

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # Accessing private member using name mangling
        print(self._Base__c)  

    def __hello(self , name):
        print("Hello",self.name)
    
    def welcome(self, name):
        self.name = name
        self.__hello(self.name)
        #print("Hello",self.name)

# Create an object of Base class
obj1 = Base()
print(obj1.a)  # This will print "Gurukul"


# Create an object of Derived class
obj2 = Derived()  # This will print the private member __c
obj2.__hello("Mukesh")
obj2.welcome("Mukesh")