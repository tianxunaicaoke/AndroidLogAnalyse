import os

def readFile(fileName):
    with open(fileName) as f:
        print(f)
        while f.readline():
            line = f.readline()
            if "(am_crash)" in line:
                print(line)
                print(fileName)



def filterTheCurrentFolder(folerName):
    for maindir, subdir, file_name_list in os.walk(folerName):
        print(maindir)
        print(subdir)
        print(file_name_list)
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if '.txt' in apath:
                readFile(apath)


if __name__ == '__main__':
    filterTheCurrentFolder("D:\\BugAnalysis\\DEN-49034\\logcat")