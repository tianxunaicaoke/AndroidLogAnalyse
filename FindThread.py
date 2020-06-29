import sys

import BaseUtil


def readfile(file_name):
    f = open(file_name)
    BaseUtil.get_target_log_position(file_name, r'(\s+\d{3,8}){2}\s+\w+')
    line = f.readline()
    thread_id = []
    count = []
    while line:
        id = BaseUtil.get_target_log_position(line, 5)
        if id not in thread_id:
            thread_id.append(id)
            count.append(1)
        else:
            count[thread_id.index(id)] = count[thread_id.index(id)] + 1
        line = f.readline()
    f.close()
    return thread_id, count


def writ_to_file(file_name, a, b):
    f = open(file_name, 'w')
    for (a1, a2) in zip(a, b):
        s1 = "ThreadId is " + a1 + "      "
        str2 = "count is " + str(a2) + "\n"
        str3 = s1.ljust(10, " ") + str2
        f.writelines(str3)
    f.close()


def _main(argv):
    pass


if __name__ == '__main__':
    _main(sys.argv)

