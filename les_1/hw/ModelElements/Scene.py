from PoligonalModel import PoligonalModel
from Flash import Flash
from Camera import Camera


class Scene:
    id: int
    models: list[PoligonalModel]
    flashes: list[Flash]
    cameras: list[Camera]


    def __init__(self, models: PoligonalModel, cameras: Camera, flashes: Flash) -> None:
        if len(models) == 0:
            raise ValueError('Количество моделей не должно быть меньше 1')
        if len(cameras) == 0:
            raise ValueError('Количество камер не должно быть меньше 1')
        for camera in cameras:
            self.cameras.append(camera)
        for model in models:
            self.models.append(model)
        for flash in flashes:
            self.flashes.append(flash)
        
    def method_1(*args):
        return args
    
    def method_2(*args, **kwargs):
        return args, kwargs