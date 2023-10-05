import zope.interface

from ModelElements.PoligonalModel import PoligonalModel
from ModelElements.Flash import Flash
from ModelElements.Camera import Camera
from ModelElements.Scene import Scene
from IModelChangedObserver import IModelChangedObserver
from IModelCharger import IModelChanger


# Заглушки - значения по умолчанию для композиции классов
__DEFAULT_ANGEL = None
__DEFAULT_LOCATION = None
__DEFAULT_COLOR = None
__DEFAULT_POWER = 1.0
__DEFAULT_TEXTURE = None

class ModelStore:
    zope.interface.implementer(IModelChanger)

    models: list[PoligonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    __change_observers: list[IModelChangedObserver]

    def __init__(self, change_observers: list[IModelChangedObserver]) -> None:
        model = PoligonalModel([__DEFAULT_TEXTURE])
        camera = Camera(__DEFAULT_LOCATION, __DEFAULT_ANGEL)
        flash = Flash(__DEFAULT_LOCATION, __DEFAULT_ANGEL, __DEFAULT_COLOR, __DEFAULT_POWER)
        self.models.append(model)
        self.scenes.append(Scene([model], [camera], [flash]))
        self.flashes.append(flash)
        self.cameras.append(camera)
        for change_observer in change_observers:
            self.__change_observers.append(change_observer)

    def get_scene(self, id: int):
        ...
        return self.scenes[id]
    
    def notify_change(sender: IModelChanger):
        ...