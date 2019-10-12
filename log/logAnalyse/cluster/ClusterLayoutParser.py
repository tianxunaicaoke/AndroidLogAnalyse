import xml.dom.minidom as xmldom

import sys

from log.logAnalyse.cluster.DrawLayout import draw_ract, draw

cid = 'gm.res:cluster_id'
cx = 'gm.res:cluster_locationX'
cy = 'gm.res:cluster_locationY'
cw = 'gm.res:cluster_sizeW'
ch = 'gm.res:cluster_sizeH'
ca = 'gm.res:cluster_alpha'
cz = 'gm.res:cluster_zOrder'

n = 38
m = 17
map = [["0"] * n for i in range(m)]
color = ["30","31","32","33","34","35","36","37"]


def get_all_element(xmlfilepath):
    domobj = xmldom.parse(xmlfilepath)
    elementobj = domobj.documentElement
    nodes = elementobj.childNodes
    i = 0
    for node in nodes:
        if node.nodeType == 1:
            i = i + 1
            get_element_attrs(node, color[i % 8])


def get_element_attrs(node, color):
    if node.getAttribute(ca) == '100':
       draw_ract(map, int(int(node.getAttribute(cx)[:-2])/10), int(int(node.getAttribute(cy)[:-2])/10), int(int(node.getAttribute(cw)[:-2])/10),
              int(int(node.getAttribute(ch)[:-2])/10), color)
       print("\033["+color+";0m"+node.getAttribute(cid)+"\033[0m")


def draw_layout(path):
    get_all_element(path)
    draw(map)


if __name__ == '__main__':
    get_all_element("./clusterLayout/res/layout-w372dp-h160dp/ipc_nav_agv.xml")
    draw(map)


