"""
WAP to store two points as tuples and calculate the distance between them.
"""

p1 = (3, 4)
p2 = (7, 1)

distance = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
print(f"The distance between the points is: {distance}")
