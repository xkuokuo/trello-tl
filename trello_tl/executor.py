from .util import isPositiveInt

class Executor:
    def __init__(self, dao, display, config):
        self.dao = dao
        self.display = display
        self.config = config

    def run(self, args):
        if args.operation == "lb":
            self._list_boards()
        elif args.operation == "db":
            self._display_board(args.board_identifier)
        else:
            raise Exception("Unsupported Opeartion{}".format(args.operation))

    def _list_boards(self):
        self.display.display_board_list(self.dao.list_boards())

    def _display_board(self, board_identifier):
        if not board_identifier:
            # try to retrieve default baard name
            if "board_id" in self.config:
                board = self.dao.get_board(self.config["board_id"])
                self.display.display_board(board)
            else:
                raise Exception("No default board id found. Must provide a valid board id")
        else:
            # TODO: fuzzy search retrieve
            board_id = self._get_board_id_from_board_name(board_identifier)
            board = self.dao.get_board(board_id)
            self.display.display_board(board)

    def _get_board_id_from_board_name(self, board_identifier):
        board_summaries = self.dao.list_boards()
        if isPositiveInt(board_identifier) and int(board_identifier) < len(board_summaries):
            return board_summaries[int(board_identifier)].board_id
        else:
            matched_res = [b for b in board_summaries if board_identifier in b.board_name]
            if len(matched_res) > 0:
                return matched_res[0].board_id
            else:
                raise Exception("Can't find board with identifier {}".format(board_identifer))
