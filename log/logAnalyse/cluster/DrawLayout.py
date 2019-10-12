
start = '\033['
color_end = ';0m'
end = '\033[0m'


def draw_line(map, x, y, w, color):
    if w == 0:
        w = 1
    for i in range(1, w):
        map[y][x + i] = color


def draw_col(map, x, y, h, color):
    if h == 0:
        h = 1
    for i in range(1, h):
        map[y + i][x] = color+"|"


def draw(map):
    n = len(map)
    m = len(map[0])
    for i in range(0, n):
        for j in range(0, m):
            if "|" in map[i][j]:
                print(start + (map[i][j])[:-1] + color_end + "|" + end, end="")
            elif map[i][j] is not "0":
                 print(start + map[i][j] + color_end + "-" + end, end="")
            elif map[i][j] is "0":
                 print(" ", end="")
        print("")


def draw_ract(map, x, y, w, h, color):
    draw_line(map, x, y, w,color)
    draw_col(map, x, y, h,color)
    draw_line(map, x, y + h, w,color)
    draw_col(map, x + w, y, h,color)

if __name__ == '__main__':
    n = 50
    m = 50
    map = [["0"] * n for i in range(m)]
    draw_ract(map,0,0,18,16,"32")
    draw(map)
