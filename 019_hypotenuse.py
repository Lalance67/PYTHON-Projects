# Given the two perpendicular sides a and b, calculate the hypotenuse.
import math
a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt((a ** 2) + (b ** 2))
print(f"{c:.2}")