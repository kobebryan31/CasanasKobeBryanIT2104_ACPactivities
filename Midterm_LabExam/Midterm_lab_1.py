import math

radius = float(input("Enter the radius of the sphere: "))

surface_area = 4 * math.pi * (radius ** 2)

volume = (4/3) * math.pi * (radius ** 3)

print(f"Surface Area of the sphere: {surface_area:.2f}")
print(f"Volume of the sphere: {volume:.2f}")
