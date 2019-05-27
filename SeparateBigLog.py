import os

import BaseUtil


def read_file_and_separate(file_name):
    f = open(file_name)
    line = f.readline()
    index = 0
    name_index = 0
    s1 = "separate" + str(name_index) + ".txt"
    file = open(s1, 'w')
    while line:
        index = (index + 1) % 50000
        line = f.readline()
        file.writelines(line)
        if index == 49999:
            name_index = name_index + 1
            file.close()
            s1 = file_name + "separate" + str(name_index) + ".txt"
            file = open(s1, 'w')
    file.close()
    f.close()


def filter_the_current_folder(folder_name):
    for maindir, subdir, file_name_list in os.walk(folder_name):
        for filename in file_name_list:
            path = os.path.join(maindir, filename)
            if '.log' in path and BaseUtil.get_doc_size(path) > 10:
                read_file_and_separate(path)


if __name__ == '__main__':
    filter_the_current_folder("D:\\Users\\xtian\\PycharmProjects\\LogUtil")
