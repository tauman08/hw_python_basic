# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#

#import task_1 as t1
import os
def parsing_yaml(text):
    list_dir = []
    lavels = {}
    separator = ''
    strpath = ''
    previos_level = 0
    previos_path =''

    for line in text:
        num_current_dir = line.find("|--")
        lavel = int(num_current_dir / 3)
        name_current_dir = line[num_current_dir + 3:].strip()
        if strpath != '':
            list_dir.append(strpath)
        if previos_level < lavel:
            previos_path = strpath
            lavels.setdefault(previos_level,previos_path)
            lavels[previos_level] = previos_path
        elif previos_level == lavel:
            strpath = previos_path #strpath[:strpath.rfind(separator) + 1]
        elif previos_level > lavel:
            strpath = lavels[max(0,lavel-1)]
        strpath += separator + name_current_dir
        if separator == '':
            separator = "\\"
        previos_level = lavel
    if strpath != '':
        list_dir.append(strpath)
    return list_dir



os.chdir(r'E:\course\GB\python\basic python\Home work\dz_7')
with open('config.yaml') as f:
   text = f.readlines()

list_dir = parsing_yaml(text)
for path in list_dir:
    if os.path.exists(path) == False:
        os.mkdir(path)

