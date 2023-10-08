from abc import ABC, abstractmethod


class ItemFabric(ABC):

    @abstractmethod
    def create_item(self):
        ...

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):

    @abstractmethod
    def open(self):
        ...
