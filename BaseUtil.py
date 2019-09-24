import os


def get_string_by_index(line, index):
    value = line.split()
    return value[index]


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
