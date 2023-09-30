class Circle:
    def __init__(self, radius_list):
        self.__pi = 3.141  # Private variable for pi
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = self.__pi * (radius ** 2)
            areas.append(area)
        return areas

    def calculate_circumference(self):
        circumferences = []
        for radius in self.radius_list:
            circumference = 2 * self.__pi * radius
            circumferences.append(circumference)
        return circumferences

if __name__ == "__main__":
    radii = [10, 501, 22, 37, 100, 999, 87, 351]
    
    circle = Circle(radii)
    
    areas = circle.calculate_area()
    circumferences = circle.calculate_circumference()
    
    for i, radius in enumerate(radii):
        print(f"Circle {i + 1} - Radius: {radius}")
        print(f"   Area: {areas[i]}")
        print(f"   Circumference: {circumferences[i]}")