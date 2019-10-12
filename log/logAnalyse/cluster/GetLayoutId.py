def get_layout_id(name, files):
    layout = ""
    for file in files:
        f = open(file)
        start = False
        for line in f.readlines():
            if name in line:
                start = True
            if start and "break" in line:
                break
            if start and "layoutId" in line:
                layout= layout + " "+(line.split()[-1])
                break

        f.close()
    return layout

if __name__ == '__main__':
    print (get_layout_id("nav_menu",
                  ["clusterLayout/ClusterLayoutFocus.txt", "clusterLayout/ClusterLayoutUnFocus.txt", "clusterLayout/HudLayout.txt"]))
