from Poligon import Poligon
from Texture import Texture


class PoligonalModel:
    poligons: list[Poligon]
    textures: list[Texture]

    def __init__(self, textures: Texture) -> None:

        # if len(self.poligons) == 0:
        #     raise ValueError('Количество полигонов не должно быть меньше 1')
        # данное условие здесь становится неуместным, т.к. присутствует композиция класса Poligon,
        # что исключает нулевое количество экземпляров Poligon

        self.poligons.append(Poligon())
        for texture in textures:
            self.textures.append(texture)
