import sys

from BaseUtil import is_file


def remove_line(file_name, template_name):
    f = open(file_name)
    line = f.readline()
    s1 = file_name + "temp.txt"
    file_n = open(s1, 'w')
    if is_file(template_name):
        template = open(template_name)
        template_line = template.readlines()
    else:
        template_line = template_name
    while line:
        line = f.readline()
        if not check(template_line, line):
            file_n.writelines(line)
    if is_file(template_name):
        template.close()
    file_n.close()
    f.close()


def check(lines, line):
    for string in lines:
        string = string.replace("\n", "")
        if string in line or line == "\n":
            return True
    return False


def _main(argv):
    remove_line(argv[1], argv[2])


if __name__ == '__main__':
    _main(sys.argv)
