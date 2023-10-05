from Staff.Point3D import Point3D


class Poligon:

    def __init__(self, *args) -> None:
        if len(args) == 0:
            raise ValueError('Количество 3D-точек должно быть больше 0')
        self.points: tuple(Point3D) = args
