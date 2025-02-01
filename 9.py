import math
def sphere(radius):
    return (4/3) * math.pi * radius**3 
radius = float(input())
volume = sphere(radius)
print(f"The volume is: {volume}")
