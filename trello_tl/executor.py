class Executor:
    def __init__(self, dao, display):
        self.dao = dao
        self.display = display

    def run(self, args):
        if args.operation == "db":
            self._display_board(args.board_name)
        else:
            raise Exception("Unsupported Opeartion{}".format(args.operation))


    def _display_board(self, board_name):
        if not board_name:
            # try to retrieve default baard name
            pass
        else:
            # TODO: fuzzy search retrieve
            board_id = self._get_board_id_from_board_name(board_name)
            board = self.dao.get_board(board_id)
            print("Display board:")
            print(board)


    def _get_board_id_from_board_name(self, board_name):
        # TODO fuzzy match board name with board id
        return board_name
