import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
    
    for i, radius in enumerate(radii_list):
        circle = Circle(radius)
        area = circle.calculate_area()
        perimeter = circle.calculate_perimeter()
        
        print(f"Circle {i + 1} with radius {radius}:")
        print(f"   Area: {area}")
        print(f"   Perimeter (Circumference): {perimeter}")