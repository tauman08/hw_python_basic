# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


import os
def make_dir(dir,path):
    for key,value in dir.items():
        if os.path.exists(key) == False:
            os.mkdir(key)
        if value != None:
            os.chdir(key)
            for sub_dir in value:
                make_dir(sub_dir,os.getcwd())
    os.chdir(path)

if __name__ == '__main__':
    list_dir = {'my_project':[{'settings' : None}
        ,{'mainapp' : None}
        ,{'adminapp' : None}
        ,{'authapp' : None}]}
    os.chdir(r'E:\course\GB\python\basic python\Home work\dz_7')
    make_dir(list_dir,os.getcwd())
