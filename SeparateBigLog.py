import os

def readFileAndSeparate(fileName):
    f = open(fileName)
    line = f.readline()
    index = 0;
    nameIndex = 0;
    s1="separate" + str(nameIndex)+".txt"
    file = open(s1, 'w')
    while line:
        index = (index + 1) % 50000
        line = f.readline()
        file.writelines(line)
        if index == 49999:
            nameIndex = nameIndex + 1;
            file.close()
            s1=fileName+"separate" + str(nameIndex)+".txt"
            file = open(s1, 'w')
    file.close()
    f.close()

def filterTheCurrentFolder(folerName):
    for maindir, subdir, file_name_list in os.walk(folerName):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if '.log' in apath and getDocSize(apath)>10:
                readFileAndSeparate(apath)


def formatSize(bytes):
        bytes = float(bytes)
        kb = bytes / 1024
        M = kb / 1024
        return M


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    filterTheCurrentFolder("D:\\Users\\xtian\\PycharmProjects\\LogUtil")