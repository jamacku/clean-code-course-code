class Point:
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


class Rectangle:
    def __init__(self, start_point, width, high):
        self.start_point = start_point
        self.width = width
        self.high = high

    def area(self):
        return self.width * self.high

    def calculate_unknown_coordinates(self):
        top_right_x = self.start_point.coordinate_x + self.width
        bottom_left_y = self.start_point.coordinate_y + self.high
        print('Starting Point (X)): ' + str(self.start_point.coordinate_x))
        print('Starting Point (Y)): ' + str(self.start_point.coordinate_y))
        print('End Point X-Axis (Top Right): ' + str(top_right_x))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left_y))


def create_rectangle():
    start_point = Point(50, 100)
    rectangle = Rectangle(start_point, 90, 10)

    return rectangle


rectangle = create_rectangle()

print(rectangle.area())
rectangle.calculate_unknown_coordinates()
