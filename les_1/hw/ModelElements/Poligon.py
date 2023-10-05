from Stuff.Point3D import Point3D


class Poligon:

    points: list[Point3D]

    def __init__(self, point: Point3D) -> None:
        self.points.append(point)
