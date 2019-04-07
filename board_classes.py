import random


class Board:

    def __init__(self, size):
        self.size = size
        self.objects_on_board = {}
        self.__create_empty_pool__()

    def add_object_to_board(self, board_object):
        self.objects_on_board[board_object.position] = board_object

    def remove_object_from_board(self, board_object):
        temp_position = board_object.position
        del self.objects_on_board[board_object.position]
        self.add_object_to_board(EmptyObject(self.find_free_pk(), temp_position))

    def show_all_animals_on_board(self):
        for y in range(1, self.size+1):
            object_list = []
            i = 0
            for x in range(1, self.size+1):
                object_list.append(self.objects_on_board[(x, y)].abbr)
                i += 1
                if i == self.size:
                    print(object_list)
        print(self.size * 5 * "-")

    def get_animals(self):
        return [animal for animal in self.objects_on_board.values() if
                animal.kind == 'carnivore' or
                animal.kind == 'herbivore']

    def get_food(self):
        return [food for food in self.objects_on_board.values() if
                food.kind == 'meat' or
                food.kind == 'plant']

    def find_empty_position(self):
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.kind is 'empty'])

    def find_free_pk(self):
        i = 1
        while True:
            if i not in [value.pk for value in self.objects_on_board.values()]:
                return i
            i += 1

    def __create_empty_pool__(self):

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.add_object_to_board(EmptyObject(self.find_free_pk(), (x, y)))


class EmptyObject:

    def __init__(self, pk, position):
        self.pk = pk
        self.position = position
        self.kind = 'empty'
        self.abbr = 'E'
        self.is_animal = False
