# Build a basic object Orientated Calculator
# phase 1: build a simple calculator class containing add, subtract, multiply, divide.
# phase 2: expand by creating:
# Divisible by method that returns true or false dependent on the outcome
# Work out and return the area of a triangle
# inch to cm converter


class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
            
    def devide(self, a, b):
        return a / b

    def divisible_by(self, a, b):
        return a % b == 0 
    
    def inch_to_cm(self, a):
        return a * 2.54