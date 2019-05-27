import os
from .util import align_str_len

DEFAULT_MAX_WIDTH = 20

class Display:
    def __init__(self, config={}):
        if "max_width" in config:
            self.max_width = int(config["max_width"])
        else:
            self.max_width = DEFAULT_MAX_WIDTH

    def display_card(self, card):
        self.print_style("Title:", fg_color=30, bg_color=43, end="\n")
        self.print_style(card.card_name)
        self.print_style("Description:", fg_color=30, bg_color=43, end="\n")
        self.print_style(card.desc)

    def display_board_list(self, board_list):
        os.system("clear")
        for index, board_summary in enumerate(board_list):
            self.print_style("{}. {}".format(index, board_summary))

    def display_board(self, board):
        os.system("clear")
        self.print_style("Board: {}".format(board.board_name, board.board_id),
                         fg_color=40, bg_color=33)
        max_len = 0
        for l in board.lists:
            if max_len < len(l.card_summaries):
                max_len = len(l.card_summaries)

        for i,l in enumerate(board.lists):
            self.print_style(align_str_len("  {}. {}  ".format(str(i).rjust(2), l.list_name), self.max_width),
                             fg_color=30, bg_color=43, end="")
        print()

        for i in range(max_len):
            for j,l in enumerate(board.lists):
                if i < len(l.card_summaries):
                    self.print_style(align_str_len(" ({}). {} ".format(str(i), l.card_summaries[i].card_name), self.max_width), end="")
                else:
                    self.print_style("".ljust(self.max_width), end="")
            print()

    def print_style(self, s, fg_color="", bg_color="", text_style="", end="\n"):
        sc = "\033[{};{};{}m".format(text_style, fg_color, bg_color)
        print(sc + s, end=end)
