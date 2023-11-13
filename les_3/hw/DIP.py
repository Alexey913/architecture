from abc import ABC, abstractmethod
from math import pi

# Принцип DIP

class Engine(ABC):

    @abstractmethod
    def start():
        ...

    @abstractmethod
    def type_engine():
        ...


class Car(ABC):

    engine: Engine

    @abstractmethod
    def start_car():
        ...

    @abstractmethod
    def about_car():
        ...


class Diesel(Engine):

    def start(self):
        print('Двигатель запущен')

    def type_engine(self):
        print('Дизельный двигатель')


class Electric(Engine):

    def start(self):
        print('Двигатель включен')

    def type_engine(self):
        print('Электродвигатель')


class Petrol(Engine):

    def start(self):
        print('Зажигание включено. Двигатель запущен')

    def type_engine(self):
        print('Бензиновый двигатель')


class Lada(Car):

    def __init__(self) -> None:
        self.engine = Petrol()

    def start_car(self):
        self.engine.start()

    def about_car(self):
        self.engine.type_engine()


class Honda(Car):

    def __init__(self) -> None:
        self.engine = Electric()

    def start_car(self):
        self.engine.start()

    def about_car(self):
        self.engine.type_engine()

if __name__ == '__main__':

    # К принципу DIP
    lada = Lada()
    lada.start_car()
    lada.about_car()

    print('-----------')

    honda = Honda()
    honda.start_car()
    honda.about_car()