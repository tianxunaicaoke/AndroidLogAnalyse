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