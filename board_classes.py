class Board:

    def __init__(self, size):
        self.size = size
        self.objects_on_board = {}
        self.__create_empty_pool__()

    def add_object_to_board(self, object):
        self.objects_on_board[object.pk] = vars(object)
        # self.objects_on_board[]["position"] = position
        # self.objects_on_board[pk]["kind"] = kind

    def show_all_animals_on_board(self):
        for x in range(1, self.size):
            i = 0
            for y in range(1, self.size):
                print('')
                i += 1
                if i == self.size:
                    print('\n')
        pass

    def __create_empty_pool__(self):

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.add_object_to_board(EmptyObject(self.__find_free_pk__() , (x, y), 'empty'))

    def __find_free_pk__(self):
        i = 1
        while True:
            if i not in self.objects_on_board.keys():
                return i
            i += 1



class EmptyObject:

    def __init__(self, pk, position, kind):
        self.pk = pk
        self.position = position
        self.kind = kind
        self.abbr = kind[0]
