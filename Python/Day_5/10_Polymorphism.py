
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
          print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
         newReal = self.real + num2.real
         newImg = self.img + num2.img
         return Complex(newReal, newImg)



com1 = Complex(1,3)
com1.showNumber()

com2 = Complex(3,6)
com2.showNumber()

# com3 = com1.add(com2)
# com3.showNumber()

num4 = com1 + com2

num4.showNumber()


# print(1+2)
# print("Guru" + "Kul") # Concatination
# print([1,2,3] + [4,5,6]) # Merge

# print(type([1,2,3] ))


