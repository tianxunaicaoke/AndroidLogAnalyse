import os


def get_string_by_index(line, index):
    value = line.split()
    return value[index]


def is_file(file_name):
    return os.path.isfile(file_name)


def format_size(bytes):
    bytes = float(bytes)
    kb = bytes / 1024
    m = kb / 1024
    return m


def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return format_size(size)
    except Exception as err:
        print(err)


def get_file_name(path):
    file_list = []
    for maindir, subdir, file_name_list in os.walk(path):
        file_list = file_name_list
        break
    return file_list


def writer(file_name, information):
    f = open(file_name, "w")
    for info in information:
        f.writelines(info + "\n")
    f.close()
    pass


def remove_duplicate_line_by_iteam(file_name, item_index):
    f = open(file_name + ".txt")
    f1 = open(file_name + "new.txt", "w")
    exist_item = []
    for info in f.readlines():
        if info.split()[item_index] not in exist_item:
            exist_item.append(info.split()[item_index])
            f1.writelines(info)
    f.close()
    f1.close()
    pass


def remove_temp_file(path_list):
    for p in path_list:
        if os.path.exists(p):
            os.remove(p)
    pass


def get_col_by_index(path_list, index):
    f = open(path_list)
    back = []
    for line in f.readlines():
        back.append(line.split()[index])
    return back


def is_log_file(file_name):
    if '.txt' in file_name or '.log' in file_name:
        return True
    else:
        return False
