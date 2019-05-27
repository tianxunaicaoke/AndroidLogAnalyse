from log.logAnalyse.base.BaseFrame import BaseWriter, BaseProcessor, BaseTemplate, BaseDistributor, BaseReader, \
    BaseFrame


class CrashReader(BaseReader):
    def readfile(self, cl_distributor):
        f = open(self.file_name)
        cl_distributor.distributor(f)
        f.close()
        pass


class ClusterProcessor(BaseProcessor):
    def processor(self, writer):
        information = self.get_base_information("died.txt")
        writer.writer("Crash report", information)
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
    logString = '../../log/'
    outString = '../../Output/'
    reader = BaseReader(logString + 'logcat.txt')
    template = BaseTemplate("template.txt")
    distributor = BaseDistributor(template)
    writer = BaseWriter(outString + 'response.txt')
    process = ClusterProcessor()
    base_frame = BaseFrame()
    base_frame.excuter(reader, distributor, writer, process)
