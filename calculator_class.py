# creating a Calculator class
class Calculator:

    # function for addition
    def add(self, a, b):
        return a + b
    
    # function for subtraction
    def subtract(self, a, b):
        return a - b

    # function for multiplication
    def multiply(self, a, b):
        return a * b
            
    # function for division
    def devide(self, a, b):
        return a / b

    # function to check if a is divisible by b using %, modulus
    def divisible_by(self, a, b):
        return a % b == 0 