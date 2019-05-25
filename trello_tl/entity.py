class Card:
    """Entity class for Trello card object

    Reference: https://developers.trello.com/reference#cards-1
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content


class CardSummary:
    def __init__(self, card_name, card_id):
        self.card_name = card_name
        self.card_id = card_id

    def __str__(self):
        return "Card: {} ({})".format(self.card_name, self.card_id)

    def __repr__(self):
        return "Card: {} ({})".format(self.card_name, self.card_id)


class List:
    """ Entity class for Trello List json entity returned by Trello api

    Reference: https://developers.trello.com/reference#lists
    """
    def __init__(self, list_name, list_id, card_summaries):
        self.list_name = list_name
        self.list_id = list_id
        self.card_summaries = card_summaries

    def __str__(self):
        return "List: {} ({})\n Cards: {}\n".format(self.list_name, self.list_id, self.card_summaries)

    def __repr__(self):
        return "List: {} ({})\n Cards: {}\n".format(self.list_name, self.list_id, self.card_summaries)

class ListSummary:
    def __init__(self, list_name, list_id):
        self.list_name = list_name
        self.list_id = list_id

    def __str__(self):
        return "List: {} ({})".format(self.list_name, self.list_id)

    def __repr__(self):
        return "List: {} ({})".format(self.list_name, self.list_id)


class Board:
    """Entity class for Trello card object

    Reference: https://developers.trello.com/reference#boards-2
    """

    def __init__(self, board_name, board_id, lists):
        self.board_name = board_name
        self.board_id = board_id
        self.lists = lists

    def __str__(self):
        return "Board: {} ({})\n List: {}".format(self.board_name, self.board_id, self.lists)

    def __repr__(self):
        return "Board: {} ({}) List: {}".format(self.board_name, self.board_id, self.lists)


class BoardSummary:
    def __init__(self, board_name, board_id):
        self.board_name = board_name
        self.board_id = board_id

    def __str__(self):
        return "Board: {} ({})".format(self.board_name, self.board_id)

    def __repr__(self):
        return "Board: {} ({})".format(self.board_name, self.board_id)
