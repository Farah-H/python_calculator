from calculator_class import Calculator



calculator_object = Calculator()

a = float(input('What number would you like to convert to inches'))
inches = round(calculator_object.multiply(a, 2.54),2)

print( f' {a} cm = {inches} inches (to 2 decimal places).')