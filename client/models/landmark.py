class PoseLandmark:
    def __init__(self, x, y, z, visibility):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__visibility = visibility

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value