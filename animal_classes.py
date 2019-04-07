import random


class Animal:

    def __init__(self, pk, position, kind):
        self.pk = pk
        self.position = position
        self.kind = kind

        self._wanna_mate = False
        self._wanna_mate = random.randint(80, 101)

        self.__is_hungry = False
        self.__hungry_status = random.randint(60, 101)

    def move(self, board, end_position):
        self.position = end_position
        board.objects_on_board[self.pk]["position"] = end_position


class Carnivore(Animal):

    def attack(self):
        pass


class Herbivore(Animal):

    # def __init__(self, pk, position, wanna_mate_status, wanna_mate,
    #              is_hungry, hungry_status, kind):
    #
    #     super().__init__(pk, position, wanna_mate_status,
    #                      wanna_mate, is_hungry, hungry_status)
    pass



