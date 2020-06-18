import sys

import BaseUtil
from Decorators import apply_for_folder


def read_file_and_separate(file_name):
    if BaseUtil.is_log_file(file_name) and BaseUtil.get_doc_size(file_name) > 10:
        f = open(file_name)
        line = f.readline()
        index = 0
        name_index = 0
        s1 = file_name + "separate" + str(name_index) + ".txt"
        file_n = open(s1, 'w')
        while line:
            line = f.readline()
            index = (index + 1) % 50000
            file_n.writelines(line)
            if index == 49999:
                name_index = name_index + 1
                file_n.close()
                s1 = file_name + "separate" + str(name_index) + ".txt"
                file_n = open(s1, 'w')
        file_n.close()
        f.close()


@apply_for_folder
def read_folder_and_separate(folder_name):
    read_file_and_separate(folder_name)


def _main(argv):
    if argv[1] == '-f':
        read_folder_and_separate(argv[2])
    else:
        read_file_and_separate(argv[1])
    pass


if __name__ == '__main__':
    _main(sys.argv)
