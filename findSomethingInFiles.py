import os


def readFile(fileName):
    with open(fileName) as f:
        line = f.readline()
        while line:
            try:
                line = f.readline()

                if find_what in line:
                    print(fileName)
                    print(line)

            except UnicodeDecodeError as e:
                continue


def filterTheCurrentFolder(folerName):
    for maindir, subdir, file_name_list in os.walk(folerName):

        for filename in file_name_list:
            if 'txt' in filename:
                apath = os.path.join(maindir, filename)
                readFile(apath)

        break


if __name__ == '__main__':
    find_what = "process id"    # process id:
    file_path = "D:\BugAnalysis\DEN-48730\logcat"
    filterTheCurrentFolder(file_path)
