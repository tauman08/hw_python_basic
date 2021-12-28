# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них
# словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз меньше объема ОЗУ.

import json

with open('ФИО.csv',encoding='utf-8') as f:
    text_name = f.read()
    list_name = text_name.split('\n')
with open('хобби.csv',encoding='utf-8') as f:
    text_hobby = f.read()
list_hobby = text_hobby.split('\n')

if len(list_hobby) > len(list_name):
    print('1')
else:
    dict_form ={}
    for i,str_name in enumerate(list_name):

        str_key = ' '.join(str_name.split(','))
        dict_form.setdefault(str_key,None)
        if i < len(list_hobby):
            dict_form[str_key] = list_hobby[i]

    with open('result.json','w') as f:
        json.dump(dict_form,f)

    with open('result.json') as f:
        date = json.load(f)

    print(date)

