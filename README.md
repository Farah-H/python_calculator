# Python OOP Task - Calculator
## Task 
Build a basic object Orientated Calculator
__phase 1:__ build a simple calculator class containing add, subtract, multiply, divide.

__phase 2:__ expand by creating:
- Divisible by method that returns true or false dependent on the outcome
- Work out and return the area of a triangle
- inch to cm converter
__NOTE:__ Must be in class and method format

## Pre-Requisites
__Necessary:__ You must have python installed.  
__Optional:__ It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 
## Syntax
### Step 1: Create a Calculator Class with Basic Functions
```python
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
```
### Step 2: Creating a Class for Calculating Triangle Area

__In a seperate file__ import the `Calculator` class. For the purposes of practicing OOP, we are pretending built in functions don't exist and are using our calculator to carry out operations. 
```python
# importing Calculator class
from calculator_class import Calculator
```
Then we initialised this class using `super().__init__(self)` to inherit the functions from the parent class. 
```python
# creating a class to find the area of a triangle
# in the future can expand on this by including sine / cosine functions but for now it's just l*w*0.5
class Triangle(Calculator):
    
    # specifying that the class needs to take in two arguments
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
```
### Step 3: Creating a Method for Calculating Triangle Area
```python
    def find_area(self):
        area = self.devide(self.multiply(self.length, self.width), 2) # using our Calculator class
        print(f'The area of this triangle is {area}.')
```
### Step 4: Run the Methods Using a Seperate File

```python
# importing our calculator_class
from calculator_class import Calculator

# instantiating the class
calculator_object = Calculator()

# as an example, we use our calculator class to convert cms to inchhes.
a = float(input('What number would you like to convert to inches'))
inches = round(calculator_object.multiply(a, 2.54),2)

print( f' {a} cm = {inches} inches (to 2 decimal places).')
```