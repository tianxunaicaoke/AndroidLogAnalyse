import os
def getStringByindex(LineString,index):
    Value = LineString.split();
    return Value[index]

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