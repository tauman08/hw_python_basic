# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

def email_parse(address):
    result = {}
    pattern = r'^(?P<name>\w[\w_\-\.]*)@(?P<domen>[\w_\-\.]+\.[a-z]+)$'
    re_email = re.compile(pattern)
    if re_email.fullmatch(address) == None:
        raise ValueError
    res_map= list(map(lambda x: x.groupdict(),re_email.finditer(address)))
    return res_map[0]

address = '23423423.@mail.ru'
try:
    res = email_parse(address)
except ValueError as ve:
    print(f'wrong email: {address} ')
    exit()
print(res)