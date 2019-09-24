from BaseUtil import get_file_name, writer


def readfile(file_path):
    list = get_file_name(file_path)
    folder = []
    for file in list:
        f = open(file_path + "/" + file)
        cluster = ''
        hud = ''
        for line in f.readlines():
            if "HomepageView" in line:
                cluster = line.split()[-2]
            elif "HudView" in line:
                hud = line.split()[-2]
            elif 'ViewSize type="Cluster"' in line:
                cluster = cluster + " " + line.split()[-3] + " " + line.split()[-2]
            elif 'ViewSize type="Hud"' in line:
                hud = hud + " " + line.split()[-3] + " " + line.split()[-2]
        if cluster is not '':
            folder.append(cluster)
        if hud is not '':
            folder.append(hud)
        f.close()
    writer('temp/foldersize.txt', folder)
    pass

if __name__ == '__main__':
    readfile("E:/HMI-Common/hmi-common/NavHome/Platform/GMPlatform/src/main/res/xml")