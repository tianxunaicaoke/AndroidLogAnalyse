def get_template_name_by_id(id):
    file = open("TemplateXmlIds.txt")
    name = []
    for line in file.readlines():
        if id in line:
            name = line.split()[4]
            break
    return name