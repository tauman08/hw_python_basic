import os
from shutil import copytree,rmtree

if  os.path.exists('templates'):
    rmtree(r'my_project\templates')

try:
    copytree('my_project',r'my_project\templates',dirs_exist_ok=True)
except PermissionError as e:
    print(f'Ошибка доступа ({e}), каталог  не скопирован')
except OSError as e:
    print(f'ошибка файловой системы ({e}), каталог   не скопирован')
except Exception as e:
    print(f'Неизвестная ошибка {e}')