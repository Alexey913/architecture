from random import choice

from Reward import GoldGenerator, GemGenerator, DiamondGenerator, MoneyGenerator


reward_generator = [GoldGenerator(), GemGenerator(),
                    DiamondGenerator(), MoneyGenerator()]

for i in range(20):
    print(f'Сундук {i+1}')
    choice(reward_generator).open_reward()
