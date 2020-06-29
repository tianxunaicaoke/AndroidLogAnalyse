import os

from BaseUtil import get_file_name
from UnZipFiles import unzip_and_move, filter_current_folder
from LogAnalyse.base.BaseFrame import BaseWriter, BaseProcessor, BaseTemplate, BaseDistributor, BaseReader, \
    BaseFrame


class CrashReader(BaseReader):
    def __init__(self, folder_name):
        self.folder_name = folder_name
        pass

    def readfile(self, cl_distributor):
        self.delete_temp_log()
        #unzip_and_move(self.folder_name, self.folder_name)
        list = get_file_name(self.folder_name + self.getSubfileName())
        for file in list:
            f = open(self.folder_name + self.getSubfileName() + file)
            cl_distributor.distributor(f)
            f.close()
        pass

    def getSubfileName(self):
        return "main.Log.out/"

    def delete_temp_log(self):
        files = get_file_name("temp")
        for file in files:
                os.remove("temp/"+file)
        pass

    def read_file_from_all(self, cl_distributor):
        filter_current_folder(self.folder_name)
        for maindir, subdir, file_name_list in os.walk(self.folder_name):
            for fl in file_name_list:
                apath = os.path.join(maindir, fl)
                f = open(apath)
                cl_distributor.distributor(f)
                f.close()
        pass


class ClusterProcessor(BaseProcessor):
    def processor(self, writer):
        #information = self.get_base_information("temp/died.txt")
        #writer.writer("Crash report", information)
        pass

    def get_base_information(self, file_name):
        f = open(file_name)
        line = f.readline()
        information = []
        while line:
            if "com.telenav.app.denali.na" in line:
                information.append(line.split()[-1])
                break
            line = f.readline()
        f.close()
        return information

    def get_screen_information(self, file_name, information):
        f = open(file_name)
        line = f.readline()
        while line:
            if " view_i_d:" in line:
                information.append(line.split()[-1])
                break
            line = f.readline()
        f.close()
        return information

if __name__ == '__main__':
    logString = '../../Log/'
    outString = '../../Output/'
    reader = CrashReader(logString)
    template = BaseTemplate("template.txt")
    distributor = BaseDistributor(template)
    writer = BaseWriter(outString + 'response.txt')
    process = ClusterProcessor()
    base_frame = BaseFrame()
    base_frame.excuter(reader, distributor, writer, process)
