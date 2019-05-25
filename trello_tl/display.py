from .entity import Board

class Display:
    def __init__(self):
        pass

    def display_board_list(self, board_list):
        for index, board_summary in enumerate(board_list):
            print("{}. {}".format(index, board_summary))

    def display_board(self, board):
        print(board)
