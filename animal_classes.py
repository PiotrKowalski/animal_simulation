import random
from math import hypot

from board_classes import EmptyObject


class Animal(EmptyObject):

    def __init__(self, pk, position):
        super(Animal, self).__init__(pk, position)
        self.is_animal = True

        self._wanna_mate = False
        self._wanna_mate = random.randint(80, 101)

        self.__is_hungry = False
        self.__hungry_status = random.randint(60, 101)
        self.__next_goal = None

    def animal_simulation(self, board):
        print(self.__hungry_status)
        self.__to_hunger__()

        if self.__hungry_status < 0:
            board.remove_object_from_board(self)

        if self.__hungry_status <= 40:
            self.__is_hungry = True
        elif self.__hungry_status >= 80:
            self.__is_hungry = False

        if self.__is_hungry:
            food_position, food_wholesomeness = self.__find_food__(board)
            self.move(board, food_position)
            if self.position == food_position:
                self.__hungry_status += food_wholesomeness

    def move(self, board, end_position):
        if end_position is None:
            return False
        previous_position = self.position
        if self.position[0] - end_position[0] > 0 and \
                not board.objects_on_board[(self.position[0] - 1, self.position[1])].is_animal:
            self.position = (self.position[0] - 1, self.position[1])
            board.add_object_to_board(self)

        elif self.position[0] - end_position[0] < 0 and \
                not board.objects_on_board[(self.position[0] + 1, self.position[1])].is_animal:
            self.position = (self.position[0] + 1, self.position[1])
            board.add_object_to_board(self)

        elif self.position[1] - end_position[1] > 0 and \
                not board.objects_on_board[(self.position[0], self.position[1] - 1)].is_animal:
            self.position = (self.position[0], self.position[1] - 1)
            board.add_object_to_board(self)

        elif self.position[1] - end_position[1] < 0 and \
                not board.objects_on_board[(self.position[0], self.position[1] + 1)].is_animal:
            self.position = (self.position[0], self.position[1] + 1)
            board.add_object_to_board(self)

        board.add_object_to_board(EmptyObject(board.find_free_pk(), previous_position))

    def __find_food__(self, board):

        if self.kind == 'carnivore':
            compatible_food = 'meat'
        elif self.kind == 'herbivore':
            compatible_food = 'plant'

        foods = [food for food in board.get_food() if food.kind == compatible_food]
        if not foods:
            return None, None
        distances_to_food = sorted([abs(self.position[0] - food.position[0]) +
                                    abs(self.position[1] - food.position[1])
                                    for food in foods
                                    ])
        for food in foods:
            if abs(self.position[0] - food.position[0]) + \
                    abs(self.position[1] - food.position[1]) == distances_to_food[0]:

                if not None:
                    self.__next_goal = food.position
                    return food.position, food.wholesomeness

        # print(distances_to_food)
        # print(self, self.__next_goal, foods)

    def __to_hunger__(self):
        self.__hungry_status -= 5


class Carnivore(Animal):

    def __init__(self, pk, position):
        super(Carnivore, self).__init__(pk, position)
        self.kind = 'carnivore'
        self.abbr = 'C'

    def attack(self):
        pass


class Herbivore(Animal):

    def __init__(self, pk, position):
        super(Herbivore, self).__init__(pk, position)
        self.kind = 'herbivore'
        self.abbr = 'H'
