import os

def readFile(fileName):
    with open(fileName) as f:
        line = f.readline()
        while line:
            try:
                line = f.readline()

                if "pid 21479" in line:

                    print(fileName)
                    print(line)

            except UnicodeDecodeError as e:
                continue



def filterTheCurrentFolder(folerName):
    for maindir, subdir, file_name_list in os.walk(folerName):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if '.txt' in apath:
                readFile(apath)


if __name__ == '__main__':
    filterTheCurrentFolder("D:\\BugAnalysis\\DEN-49309\\out\\logcat")