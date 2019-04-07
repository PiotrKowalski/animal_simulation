from initial_functions import initialize_data_and_create_objects
from simulation_functions import start_round
from data_saver import write_to_csv, remove_csv_file

if __name__ == "__main__":

    board = initialize_data_and_create_objects()
    remove_csv_file()
    round_count = 0
    while True:
        board.show_all_animals_on_board()
        start_round(board, round_count)
        write_to_csv(board, round_count)

        round_count += 1
        if not board.get_animals():
            break
