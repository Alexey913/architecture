from IModelChangedObserver import IModelChangedObserver
from ModelElements import Camera, Flash, PoligonalModel, Scene


class ModelStore(IModelChangedObserver):

    def __init__(self) -> None:
        super().__init__()