import gzip
import os
import tarfile
import zipfile
import shutil


def un_gz(file_name):
    try:
        """ungz zip file"""
        f_name = file_name.replace(".gz", ".txt")
        g_file = gzip.GzipFile(file_name)
        open(f_name, "wb+").write(g_file.read())
        g_file.close()
    except UnicodeDecodeError as e:
        return


def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()


def un_rar(file_name):
    """unrar zip file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    os.chdir(file_name + "_files")
    rar.extractall()
    rar.close()


def filter_current_folder(folder_name):
    for maindir, subdir, file_name_list in os.walk(folder_name):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if 'main' in apath:
                if '.gz' in apath:
                    un_gz(apath)
                if '.zip' in apath:
                    un_zip(apath)

            if 'event' in apath:
                if '.gz' in apath:
                    un_gz(apath)
                if '.zip' in apath:
                    un_zip(apath)

            if 'system' in apath:
                if '.gz' in apath:
                    un_gz(apath)
                if '.zip' in apath:
                    un_zip(apath)
        break


def move_file(path):
    for maindir, subdir, file_name_list in os.walk(path):
        path = path + "/main.log.out"
        if not os.path.isdir(path):
            os.mkdir(path)

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if 'main.log' in apath and '.gz' not in apath:
                print(apath)
                shutil.move(apath, path)
        break


def unzip_and_move(in_path, out_path):
    filter_current_folder(in_path)
    move_file(out_path)

if __name__ == '__main__':
    unzip_and_move("./log/log", "./log/log")

