import csv
import os


def remove_csv_file():
    os.remove('results.csv')


def write_to_csv(board, round_count):

    food_count = len(board.get_food())
    meat_count = len([food for food in board.get_food() if food.kind == 'meat'])
    plant_count = len([food for food in board.get_food() if food.kind == 'plant'])

    animals_count = len(board.get_animals())
    carnivore_count = len([animal for animal in board.get_animals() if animal.kind == 'carnivore'])
    herbivore_count = len([animal for animal in board.get_animals() if animal.kind == 'herbivore'])

    with open('results.csv', mode='a') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        result_writer.writerow([
            round_count,
            food_count, meat_count, plant_count,
            animals_count, carnivore_count, herbivore_count
        ])
