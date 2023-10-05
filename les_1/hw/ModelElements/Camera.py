from Stuff.Point3D import Point3D
from Stuff.Angle3D import Angle3D


class Camera:

    def __init__(self, location: Point3D, angle: Angle3D) -> None:
        self.location = location
        self.angle = angle

    def rotate(self, angle: Angle3D):
        self.angle += angle

    def move(self, point: Point3D):
        self.location = point