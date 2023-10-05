from Stuff.Point3D import Point3D
from Stuff.Angle3D import Angle3D
from Stuff.Color import Color


class Flash:

    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float) -> None:
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle: Angle3D):
        self.angle += angle

    def move(self, point: Point3D):
        self.location = point