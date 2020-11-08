from calculator_class import Calculator

class Triangle(Calculator):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def find_area(self):
        area = self.devide(self.multiply(self.length, self.width), 2)
        print(f'The area of this triangle is {area}.')

# test = Triangle(4,5)
# test.find_area()