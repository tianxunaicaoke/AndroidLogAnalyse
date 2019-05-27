import BaseUtil


def readfile(file_name):
    f = open(file_name)
    line = f.readline()
    thread_id = []
    count = []
    while line:
        id = BaseUtil.get_string_by_index(line, 5)
        if id not in thread_id:
            thread_id.append(id)
            count.append(1)
        else:
            count[thread_id.index(id)] = count[thread_id.index(id)] + 1
        line = f.readline()
    f.close()
    return thread_id, count


def writ_to_file(file_name, a, b):
    file = open(file_name, 'w')
    for (a1, a2) in zip(a, b):
        s1 = "ThreadId is " + a1 + "      "
        str2 = "count is " + str(a2) + "\n"
        str3 = s1.ljust(10, " ") + str2
        file.writelines(str3)
    file.close()


if __name__ == '__main__':
    logString = "D:\\Users\\xtian\\PycharmProjects\\LogUtil\\log\\"
    fileString = "07-13"
    b, c = readfile(logString + fileString + ".txt")
    writ_to_file(logString + fileString + "-r" + ".txt", b, c)
