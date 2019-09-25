from BaseUtil import remove_duplicate_line_by_iteam, remove_temp_file
from Decorators import open_process_write_file
from log.logAnalyse.base.BaseFrame import BaseWriter, BaseProcessor, BaseTemplate, BaseDistributor, BaseReader, \
    BaseFrame

from log.logAnalyse.cluster.ClusterKeyConvertToName import get_template_name_by_id
from log.logAnalyse.cluster.GetClusterLayoutFolder import readfile


class ClusterProcessor(BaseProcessor):
    def processor(self, writer):
        view_id = self.get_base_information("temp/ClusterHmiService.txt")
        report = ["-----------------------------------------------Cluster report---------------------------------------------------",
                  "--The Cluster viewId :" + view_id,
                  "--The folder is :" + self.get_folder_size("temp/foldersize.txt", view_id),
                  "--------------------------------------------------------------------------------------------------------------"]
        writer.writer(report)
        remove_duplicate_line_by_iteam("temp/thread", 2)
        self.get_thread_information(writer.file_name)
        writer.writer(
            title="--------------------------------------------------------------------------------------------------------------")
        self.get_screen_information(writer.file_name)
        writer.writer(
            title="--------------------------------------------------------------------------------------------------------------")
        self.get_alert_information(writer.file_name)
        pass

    def get_base_information(self, file_name):
        f = open(file_name)
        line = f.readline()
        information = ""
        while line:
            if " view_i_d:" in line:
                information = line.split()[-1]
                break
            line = f.readline()
        f.close()
        return information

    def get_folder_size(self, file_name, view_id):
        f = open(file_name)
        line = f.readline()
        information=""
        while line:
            if view_id[0] in line:
                information = line.split()[-2] + line.split()[-1]
                break
            line = f.readline()
        f.close()
        return information

    @open_process_write_file("temp/screen.txt")
    def get_screen_information(line):
        information = "|--time :" + line.split()[0] + " " + line.split()[1] + "--|screen name:" + get_template_name_by_id(line.split()[-1]) + "\n"
        return True, information

    @open_process_write_file("temp/alert.txt")
    def get_alert_information(line):
        information = "|--time :" + line.split()[0] + " " + line.split()[1] + "--|alert name:" + get_template_name_by_id(line.split()[-1]) + "\n"
        return True, information

    @open_process_write_file("temp/threadnew.txt")
    def get_thread_information(line):
        thread = line.split()[2]
        return True, "--Thread ID is :" + thread + " |Start time  " + line.split()[1] + "|\n"


class ClusterWriter(BaseWriter):
    def writer(self, information="", title=""):
        f = open(self.file_name, "a")
        if title is not "":
            f.writelines(title + "\n")
        for info in information:
            f.writelines(info + "\n")
        f.close()
        pass


if __name__ == '__main__':
    logString = '../../log/'
    outString = '../../Output/'
    remove_temp_file([outString+"response.txt"])
    readfile("E:/HMI-Common/hmi-common/NavHome/Platform/GMPlatform/src/main/res/xml")
    reader = BaseReader(logString + "main.log")
    template = BaseTemplate("template.txt")
    distributor = BaseDistributor(template)
    writer = ClusterWriter(outString + "response.txt")
    process = ClusterProcessor()
    base_frame = BaseFrame()
    base_frame.excuter(reader, distributor, writer, process)
