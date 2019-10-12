class BaseReader:
    def __init__(self, file_name):
        self.file_name = file_name
        pass

    def readfile(self, cl_distributor):
        f = open(self.file_name, encoding="ANSI")
        cl_distributor.distributor(f)
        f.close()
        pass

    def getSubfileName(self):
         pass


class BaseTemplate:
    def __init__(self, file_name):
        self.file_name = file_name
        pass

    def get_template(self):
        pass

    def get_keyword_file(self):
        keyword = []
        new_file = []
        f = open(self.file_name)
        line = f.readline()
        while line:
            lines = line.split('|')
            keyword.append(lines[0].replace("\n", ""))
            new_file.append(lines[1].replace("\n", ""))
            line = f.readline()
        f.close()
        return keyword, new_file


class BaseDistributor:
    def __init__(self, template):
        self.template = template
        pass

    def distributor(self, file_name):
        keyword, file_name_list = self.template.get_keyword_file()
        writer_file = []
        for f in file_name_list:
            wf = open("temp/"+f, 'w')
            writer_file.append(wf)
        line = file_name.readline()
        while line:
            for key, f, wf in zip(keyword, file_name_list, writer_file):
                if key in line:
                    wf.writelines(line)
            line = file_name.readline()
        for wf in writer_file:
            wf.close()


class BaseWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        pass

    def writer(self, information, title=""):
        f = open(self.file_name, "w")
        f.writelines(title + "\n")
        for info in information:
            f.writelines(info + "\n")
        f.close()
        pass


class BaseProcessor:
    def __init__(self):
        pass

    def processor(self, writer):
        pass


class BaseFrame:
    def __init__(self):
        pass

    def excuter(self, reader, distributor, writer, process):
        reader.readfile(distributor)
        process.processor(writer)
