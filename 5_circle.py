from math import pi

# Getting input from user
radious = float(input("Enter radius of the circle: "))

# Finding the area and perimeter of the circle
area = (pi*radious*radious)
perimeter = (2*pi*radious)

# output
print("The area of circle is ", "%.2f" %area)
print("The perimeter of circle is", "%.2f" %perimeter)
