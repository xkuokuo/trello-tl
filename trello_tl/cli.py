import os
import sys
import argparse
import configparser
from pathlib import Path

from .api import ApiAdapter
from .credential import CredentialProvider
from .dao import Dao
from .display import Display
from .executor import Executor

def main():
    config = configparser.ConfigParser()
    config.read(os.path.join(Path.home(), ".trello_tl_config.ini"))
    api = ApiAdapter(CredentialProvider(config['Credential']))
    dao = Dao(api)
    display = Display()
    executor = Executor(dao, display, config['Default'])

    parser = argparse.ArgumentParser(description='trello-tl')
    parser.add_argument('operation', type=str, help="""Trello operations.
                        Valid values are: lb, db""")
    if len(sys.argv) < 2:
        parser.print_help()
        exit(1)

    operation = sys.argv[1]
    if operation == "lb":
        pass
    elif operation == "db":
        parser.add_argument('board_identifier', type=str, nargs="?", default="", help="""
                            Board identifier. It could be the board sequence number returned by 'tl lb', the board name, or the board id.
                            Fuzzy search supported (yeah very fuzzy XD).""")
    elif operation == "al":
        pass
    else:
        parser.print_help()

    args = parser.parse_args()
    executor.run(args)

