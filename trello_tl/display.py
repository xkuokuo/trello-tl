from .entity import Board
from .util import align_str_len

WIDTH = 20

class Display:
    def __init__(self):
        pass

    def display_board_list(self, board_list):
        for index, board_summary in enumerate(board_list):
            print("{}. {}".format(index, board_summary))

    def display_board(self, board):
        print("Board: {}".format(board.board_name, board.board_id))
        max_len = 0
        for l in board.lists:
            if max_len < len(l.card_summaries):
                max_len = len(l.card_summaries)

        for i,l in enumerate(board.lists):
            print(align_str_len("  {}. {}  ".format(str(i).rjust(2), l.list_name).ljust(WIDTH), WIDTH), end = "")

        print()

        for i in range(max_len):
            for j,l in enumerate(board.lists):
                if i < len(l.card_summaries):
                    print(align_str_len(" ({}). {} ".format(str(i), l.card_summaries[i].card_name).ljust(WIDTH), WIDTH), end = "")
                else:
                    print("".ljust(WIDTH), end = "")
            print()



    def _print_limit_length(self, s, length):
        print("{}".format(s[:length]))
