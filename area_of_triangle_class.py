# importing Calculator class
from calculator_class import Calculator

# creating a class to find the area of a triangle
# in the future can expand on this by including sine / cosine functions but for now it's just l*w*0.5
class Triangle(Calculator):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def find_area(self):
        area = self.devide(self.multiply(self.length, self.width), 2) # using our Calculator class
        print(f'The area of this triangle is {area}.')

# test = Triangle(4,5)
# test.find_area()