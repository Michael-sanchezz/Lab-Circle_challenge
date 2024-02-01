"""
Prompt the user to enter a radius; the user may enter a number with decimals (double).
Display an error if the user enters invalid data and asks the user again for a radius.
When the user enters valid data, create an instance of a Circle and then use its methods to display the Diameter, Circumference and Area.
Ask the user if the circle should grow.
If the user says yes, call the grow method and then loop back to the method calls for the formulas.
The grow method will double radius.
If the user says no, display a “goodbye” message and the radius of the circle.

Create a class named Circle to store the data about this circle. This class should contain the following:
Initialization (self, radius)
Sets the radius property
Methods
calculate_diameter()
Returns the calculated diameter
calculate_circumference()
Returns the calculated circumference
calculate_area()
Returns the calculated area
grow()
Doubles the radius property
get_radius()
Returns the radius value
"""
import math


class circle:

    def __init__(self, radius):
        self.rad = radius

    def calculate_diameter(self):
        dia = 2 * self.rad
        print(f'diameter is {dia}')
        return 2 * self.rad

    def calculate_circumference(self):
        return 2 * math.pi * self.rad

    def calculate_area(self):
        area = (math.pi * self.rad) * (math.pi * self.rad)
        return area

    def grow(self):
        inp = input("would you like your circle to grow? ")
        if inp == "y":
            print("your circle is growing!", end = "")
            self.rad = self.rad * 2
            return ''
        else:
            return "goodbye"

    def get_radius(self):
        return self.rad


user_input = (input("enter the radius "))
while user_input.isdigit() != True:
    print("invalid ")
    user_input = (input("enter the radius "))
user_input = int(user_input)

calc = circle(user_input)
print(f'diameter is {calc.calculate_diameter()}')
print(f'circumference is {calc.calculate_circumference()}')
print(f'area is {calc.calculate_area()}')
print(calc.grow())
print(f'radius is {calc.get_radius()}')
