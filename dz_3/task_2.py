# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(str_num):
    my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'
        , 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    str_res = my_dict.get(str_num)
    if str_res != None:
        return str_res
    else:
        str_res = my_dict.get(str(str_num).lower())

    if str_res != None:
        return str_res.title()
    return None

print(num_translate_adv('Eight'))