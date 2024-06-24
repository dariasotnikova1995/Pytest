class Pixel:
    def __init__(self, red, green, blue):
        for component in (red, green, blue):
            if not (0 <= component <= 255):
                raise ValueError("Pixel components must be in the range [0, 255].")
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    def __add__(self, other):
        if isinstance(other, Pixel):
            return Pixel(min(self.red + other.red, 255),
                         min(self.green + other.green, 255),
                         min(self.blue + other.blue, 255))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Pixel):
            return Pixel(max(self.red - other.red, 0),
                         max(self.green - other.green, 0),
                         max(self.blue - other.blue, 0))
        return NotImplemented

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be an integer or float.")
        if factor <= 0:
            raise ValueError("Factor must be greater than zero.")
        return Pixel(min(int(self.red * factor), 255),
                     min(int(self.green * factor), 255),
                     min(int(self.blue * factor), 255))

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be an integer or float.")
        if factor <= 0:
            raise ValueError("Factor must be greater than zero.")
        return Pixel(int(self.red / factor),
                     int(self.green / factor),
                     int(self.blue / factor))

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return self.red == other.red and self.green == other.green and self.blue == other.blue
        return NotImplemented

    def __str__(self):
        return f"Pixel object\n\tRed: {self.red}\n\tGreen: {self.green}\n\tBlue: {self.blue}"

    def __repr__(self):
        return f"Pixel({self.red}, {self.green}, {self.blue})"