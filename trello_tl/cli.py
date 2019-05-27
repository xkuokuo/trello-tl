import os
import sys
import argparse
import configparser
from pathlib import Path

from .api import ApiAdapter
from .credential import CredentialProvider
from .dao import CachedDao
from .display import Display
from .executor import Executor

def main():
    config = configparser.ConfigParser()
    config.read(os.path.join(Path.home(), ".trello_tl_config.ini"))
    api = ApiAdapter(CredentialProvider(config['Credential']))
    cache_file_path = os.path.join(Path.home(), ".trello_tl_cache.json")
    dao = CachedDao(api, cache_file_path)
    display = Display(config['Display'])
    executor = Executor(dao, display, config['Board'])

    parser = argparse.ArgumentParser(description='trello-tl')
    parser.add_argument('operation', type=str, help="""Trello operations.
                        Valid values are: lb, db, ac""")
    if len(sys.argv) < 2:
        parser.print_help()
        exit(1)

    operation = sys.argv[1]
    if operation == "lb":
        pass
    elif operation == "db":
        parser.add_argument('board_identifier', type=str, nargs="?", default="", help="""
                            Board identifier. It could be the board sequence number returned by 'tl lb', or the (partial) the board name
                            Fuzzy search supported (yeah very fuzzy XD).""")
    elif operation == "ac":
        parser.add_argument('list_identifier', type=str, default="", help="""
                            List identifier. It could be the list sequence number returned by 'tl lb', or the (partial) list name
                            Fuzzy search supported (yeah very fuzzy XD).""")
        parser.add_argument('card_name', type=str, help="Name of the new trello card")
        parser.add_argument('card_desc', type=str, nargs="?", default="", help="Some extra card description")
        pass
    else:
        parser.print_help()
        exit(1)

    args = parser.parse_args()
    executor.run(args)
    exit(0)
