from GameItemFactory import ItemFabric, IGameItem


class GoldReward(IGameItem):

    def open(self):
        print('Get gold')


class GoldGenerator(ItemFabric):

    def create_item(self):
        print('Create new item')
        return GoldReward()


class GemReward(IGameItem):

    def open(self):
        print('Get gem')


class GemGenerator(ItemFabric):

    def create_item(self):
        print('Create new item')
        return GemReward()


class DiamondReward(IGameItem):

    def open(self):
        print('Get diamond')


class DiamondGenerator(ItemFabric):

    def create_item(self):
        print('Create new item')
        return DiamondReward()


class MoneyReward(IGameItem):

    def open(self):
        print('Get money')


class MoneyGenerator(ItemFabric):

    def create_item(self):
        print('Create new item')
        return MoneyReward()