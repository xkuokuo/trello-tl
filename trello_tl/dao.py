from .entity import List, Board

class Dao:
    def __init__(self, api):
        self.api = api

    def list_boards(self):
        try:
            board_summaries = self.api.list_boards()
            return board_summaries
        except Exception as e:
            raise Exception(e, "Error Fetching Board Information From Trello XD")

    def get_board(self, board_id):
        # get lists in board
        try:
            list_summaries = self.api.list_lists(board_id)
            lists = []
            for l in list_summaries:
                card_summaries = self.api.list_cards(l.list_id)
                lists.append(List(l.list_name, l.list_id, card_summaries))
            board_summary = self.api.get_board(board_id)
            return Board(board_summary.board_name, board_id, lists)
        except Exception as e:
            raise Exception(e, "Error Fetching Board Information From Trello XD")
