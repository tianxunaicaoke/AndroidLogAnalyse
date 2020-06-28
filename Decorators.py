import os
from functools import wraps


def open_process_write_file(read_file_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = open(read_file_name)
            fw = open(args[1], "a")
            line = f.readline()
            while line:
                is_continue, line1 = func(line)
                if not is_continue:
                    break
                line = f.readline()
                fw.writelines(line1)
            f.close()
        return wrapper
    return decorator


def apply_for_folder(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for maindir, subdir, file_name_list in os.walk(args[0]):
            for filename in file_name_list:
                path = os.path.join(maindir, filename)
                args1 = change_the_first_parameter(args, path)
                func(*args1)
    return wrapper


def go_every_line_of_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f = open(args[0])
        i = 0
        for line in f.readlines():
            func(args, line, i,)
            i = i + 1
        f.close()
    return wrapper


def change_the_first_parameter(p, new_p):
    args1 = []
    for x in p:
        args1.append(x)
    args1[0] = new_p
    return args1
