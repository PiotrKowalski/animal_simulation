from food_classes import Plant, Meat
import random


def start_round(board, round_count):

    if round_count % 3 == 0:
        choice = random.choice(['meat', 'plant'])
        number_of_food = random.randint(0, 3)
        if choice == 'meat':
            for number in range(number_of_food):
                board.add_object_to_board(Meat(board.find_free_pk(), board.find_empty_position()))
        elif choice == 'plant':
            for number in range(number_of_food):
                board.add_object_to_board(Plant(board.find_free_pk(), board.find_empty_position()))

    for food in board.get_food():
        food.food_simulation(board)

    for animal in board.get_animals():
        animal.animal_simulation(board)




