# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }

def thesaurus_adv(*full_names):
    my_dict = {}
    for fname in full_names:
        key_dict = fname[fname.rfind(' ')+1]
        key_sub  = fname[0]
        if my_dict.get(key_dict) is None:
            my_dict[key_dict] = {key_sub:[fname]}
        elif my_dict[key_dict].get(key_sub) is None:
            my_dict[key_dict][key_sub] = [fname]
        else:
            my_dict[key_dict][key_sub].append(fname)

    return sorted(my_dict.items(),key=lambda x: x[0])

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))