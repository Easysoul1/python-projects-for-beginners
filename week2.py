# Pratice Exercises
# Question 1 Week 2
# Temperature conversion
print("Conversion of temperature from degreee Celsius to degree Fahrenheit and Vice versa")
temp = input("Enter your temperature \'F\' for Fahrenheit and \'C\' for Celsius : ")
if temp.upper() == "F":
       fahrenheit = float(input("Enter your Temperature in degree Fahrenheit to convert to Celsius : "))
       celsius = (fahrenheit - 32) * (5/9)
       print(f'{fahrenheit}°F = {celsius}°C')

elif temp.upper() == "C":
       celsius = float(input("Enter your Temperature in degree Celsius to convert to Fahrenheit : "))
       fahrenheit = (celsius * (9/5)) + 32
       print(f'{celsius}°C = {fahrenheit}°F')

else:
       print("Please input a valid value")



# Question 3
print("Calculating the area of Circle, Rectangle and Triangle")
shape = input("Enter the shape you want \'C\' for Circle, \'R\' for rectangle, \'T\' for triangle : ")
if shape.upper() == 'C':
       radius = float(input("Enter the radius of the circle in cm : "))
       area_of_circle = 3.142 * (radius**2)
       print(f'The Area of circle with radius {radius} is {area_of_circle}cm2')

elif shape.upper() == 'R':
       length = int(input("Enter the length of the Rectangle in cm : "))
       breath = int(input("Enter the breath of the Rectangle in cm : "))
       area_of_rectangle = length * breath
       print(f'The Area of Rectangle with the lenght {length} and breath {breath} is {area_of_rectangle}cm2')
elif shape.upper() == 'T':
       base = int(input("Enter the Base of the Triangle in cm : "))
       height =  int(input("Enter the Height of the Triangle in cm : "))
       area_of_triangle = (base * height) / 2
       print(f'The area of triangle with base {base} and height {height} is {area_of_triangle}cm2')
else:
       print("Please enter a valid shape as instruted above ")

