#Create a Rectangle class with attributes length and width. Add methods to calculate the area and perimeter of the rectangle. 
#Create two Rectangle objects and print their attributes and calculated values.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def Area(self):
        if((self.length<=0) or (self.width<=0)):
            raise ValueError("Length and width must be positive numbers.")
        return self.length*self.width

    def Perimeter(self):
        return 2*(self.width+self.length)
    
try:      
    rect1 = Rectangle(5,8)
    rect2 = Rectangle(6,12)
    area = rect1.Area()
    peri = rect2.Perimeter()
    print(area,peri)
except ValueError as e:
    print(f"An error has occurred. Details of are errors are {e}")





