import os
import sys
import argparse
from pathlib import Path

from .api import ApiAdapter
from .credential import CredentialProvider
from .dao import Dao
from .display import Display
from .executor import Executor

def main():
    print("Hello World xD")
    api = ApiAdapter(CredentialProvider(os.path.join(Path.home(), ".trello_tl_config.ini")))

    dao = Dao(api)
    display = Display()
    executor = Executor(dao, display)

    parser = argparse.ArgumentParser(description='trello-tl')
    parser.add_argument('operation', type=str, help='Trello operations. Valid values are: lb, db')
    operation = sys.argv[1]
    if operation == "lb":
        pass
    elif operation == "db":
        parser.add_argument('board_name', type=str, nargs="?", default="", help='Board names. Fuzzy search supported (yeah very fuzzy XD).')
        args = parser.parse_args()
    elif operation == "al":
        pass
    else:
        parser.print_help()

    executor.run(args)

