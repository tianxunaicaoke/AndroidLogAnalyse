def open_process_write_file(read_file_name):
    def decorator(func):
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
