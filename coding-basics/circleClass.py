# Fill in this file with the code from the Coding Basics - Classes exercise
# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius

class Circle:
    def __init__ (self,radius):
        self.radius = radius
    def circumference (self):
        pi=22/7
        circumferenceValue = pi * self.radius *2
        return circumferenceValue
    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius)+ " is " + str(myCircumference))

#Instansiasi pertama dari Kelas Circle
circle1 = Circle(2)
circle1.printCircumference()
#Instansiasi lainnya
circle2 = Circle(5)
circle2.printCircumference()
circle3 = Circle(7)
circle3.printCircumference()