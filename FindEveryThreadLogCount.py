import BaseUtil as bUtil

def readfileAndcalculateTheCount(fileName):
    f = open(fileName)
    line = f.readline()
    b =[]
    c=[]
    while line:
        a = bUtil.getStringByindex(line,5)
        if a not in b:
            b.append(a)
            c.append(1)
        else:
            c[b.index(a)]=c[b.index(a)]+1
        line = f.readline()
    f.close()
    return b,c

def writTofile(fileName,a,b):
    file = open(fileName, 'w')
    for (a1, a2) in zip(a,b):
        s1 = "ThreadId is " + a1+"      ";
        str2 = "count is " + str(a2) + "\n";
        str3 = s1.ljust(10, " ") + str2;
        file.writelines(str3)
    file.close()

if __name__ == '__main__':
    logString = "D:\\Users\\xtian\\PycharmProjects\\LogUtil\\log\\"
    fileString = "07-13"
    b,c = readfileAndcalculateTheCount(logString+fileString+".txt")
    writTofile(logString+fileString+"-r"+".txt",b,c)