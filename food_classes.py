import random

from board_classes import EmptyObject


class Food(EmptyObject):

    def __init__(self, pk, position):
        super(Food, self).__init__(pk, position)

        self.wholesomeness = random.randint(40, 61)

        self.__durability = random.randint(80, 101)

    def food_simulation(self, board):
        self.decomposition()

        if self.__durability <= 0:
            board.remove_object_from_board(self)

    def decomposition(self):
        self.__durability -= 5


class Meat(Food):

    def __init__(self, pk, position):
        super(Meat, self).__init__(pk, position)
        self.kind = 'meat'
        self.abbr = 'M'


class Plant(Food):

    def __init__(self, pk, position):
        super(Plant, self).__init__(pk, position)
        self.kind = 'plant'
        self.abbr = 'P'

