import os


def read_file(file_name):
    with open(file_name) as f:
        line = f.readline()
        while line:
            try:
                line = f.readline()
                if find_what in line:
                    print(file_name)
                    print(line)
            except UnicodeDecodeError:
                continue


def filter_the_current_folder(folder_name):
    for maindir, subdir, file_name_list in os.walk(folder_name):
        for filename in file_name_list:
                path = os.path.join(maindir, filename)
                read_file(path)
        break


if __name__ == '__main__':
    find_what = "3965"    # process id:
    file_path = "D:\BugAnalysis\DEN-49447\logcat"
    filter_the_current_folder(file_path)
