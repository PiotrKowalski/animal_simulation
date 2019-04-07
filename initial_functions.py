import csv
import random

from board_classes import Board
from animal_classes import Herbivore, Carnivore
from food_classes import Meat, Plant


def reading_initial_data_and_creating_objects():

    with open('initial_data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            size = int(row[0])
            number_of_meat = int(row[1])
            number_of_plants = int(row[2])
            number_of_carnivores = int(row[3])
            number_of_herbivores = int(row[4])

            board = Board(size)

            for i in range(1, number_of_meat+1):
                create_a_food(board, 'meat')

            for i in range(1, number_of_plants+1):
                create_a_food(board, 'plant')

            for i in range(1, number_of_carnivores+1):
                create_an_animal(board, 'carnivore')

            for i in range(1, number_of_herbivores+1):
                create_an_animal(board, 'herbivore')

            for key, value in board.objects_on_board.items():
                # if value['kind'] != 'X':
                print(key, value)


def find_free_pk(board):
    i = 1
    while True:
        if i not in board.objects_on_board.keys():
            return i
        i += 1


def create_a_food(board, kind):
    pk = find_free_pk(board)
    x = random.randint(1, board.size)
    y = random.randint(1, board.size)

    if kind == 'meat':
        food = Meat(pk, (x, y), kind)
        board.add_object_to_board(food)

    elif kind == 'plant':
        food = Plant(pk, (x, y), kind)
        board.add_object_to_board(food)


def create_an_animal(board, kind):

    pk = find_free_pk(board)
    x = random.randint(1, board.size)
    y = random.randint(1, board.size)

    if kind == 'carnivore':
        animal = Carnivore(pk, (x, y), kind)
        board.add_object_to_board(animal)

    elif kind == 'herbivore':
        animal = Herbivore(pk, (x, y), kind)
        board.add_object_to_board(animal)

