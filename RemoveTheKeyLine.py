
def remove_line(file_name, template_name):
    f = open(file_name)
    line = f.readline()
    s1 = "temp.txt"
    file = open(s1, 'w')
    template = open(template_name)
    template_line = template.readlines()
    while line:
        line = f.readline()
        if not check(template_line, line):
            file.writelines(line)
    template.close()
    file.close()
    f.close()


def check(lines, line):
    for string in lines:
        string = string.replace("\n", "")
        if string in line or line == "\n":
            return True
    return False


if __name__ == '__main__':
    remove_line("./a.txt", "./template.txt")
