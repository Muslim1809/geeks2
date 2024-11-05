class Figure:
    unit = "cm"  # Уровень класса: единица измерения

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Этот метод нужно реализовать в дочернем классе.")

    def info(self):
        raise NotImplementedError("Этот метод нужно реализовать в дочернем классе.")

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}.")

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # Приватный атрибут
        self.__width = width  # Приватный атрибут

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(
            f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}.")
# Исполняемая область
if __name__ == "__main__":
    squares = [
        Square(5),
        Square(7)
    ]
    rectangles = [
        Rectangle(5, 8),
        Rectangle(4, 6),
        Rectangle(3, 9)
    ]
    shapes = squares + rectangles

    for shape in shapes:
        shape.info()
