import sys

import BaseUtil
from Decorators import apply_for_folder


def find_in_file(file_name, find_what):
    if BaseUtil.is_log_file(file_name):
        with open(file_name) as f:
            line = f.readline()
            while line:
                try:
                    line = f.readline()
                    if find_what in line:
                        print(file_name)
                        print(line)
                except UnicodeDecodeError:
                    continue


@apply_for_folder
def find_in_folder(folder_name, find_what):
    find_in_file(folder_name, find_what)


def _main(argv):
    if argv[1] == '-f':
        find_in_folder(argv[2], argv[3])
    else:
        find_in_file(argv[1], argv[2])
    pass


if __name__ == '__main__':
    _main(sys.argv)
