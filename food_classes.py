import random


class Food:

    def __init__(self, pk, position, kind):
        self.pk = pk
        self.position = position
        self.kind = kind
        self.wholesomeness = random.randint(10, 30)

        self.__durability = random.randint(50, 101)

    def decomposition(self):
        self.__durability -= 5
        if self.__durability <= 0:
            del self


class Meat(Food):

    # def __init__(self, wholesomeness, kind):
    #     super().__init__(wholesomeness)
    #     self.kind = kind
    pass


class Plant(Food):

    # def __init__(self, wholesomeness, kind):
    #     super().__init__(wholesomeness)
    #     self.kind = kind
    pass
