import os
from functools import wraps
import BaseUtil


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
                args1 = []
                for x in args:
                    args1.append(x)
                args1[0] = path
                func(*args1)
    return wrapper
