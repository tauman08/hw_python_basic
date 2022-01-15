# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(arg1,arg2,arg3,**kwargs):
        print(f' height type : {type(arg1)},width type: {type(arg2)},depth type: {type(arg3)}')
        for arg_name,arg in kwargs.items():
            print(f'{arg_name} type : {type(arg)}')
        print(f'volume = {func.__name__}({arg1},{arg2},{arg3})')
        print(f'{func.__name__}({type(arg1)},{type(arg2)},{type(arg3)})')

        return func(arg1,arg2,arg3,**kwargs)
    return wrapper

@type_logger
def calc_volume(height,width,depth,scale=1):
    """ the function calculates the volume of the box

    arguments:
        height,width,depth
    """
    return height*width*depth*scale**3

volume = calc_volume(100,200,300,scale = 2)
print(f'volume = {volume}')

print(calc_volume.__doc__)
