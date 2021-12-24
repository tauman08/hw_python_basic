# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(char_code):
    answer =  requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if answer.ok == False:
        return None
    start_pos = answer.text.find(f'<CharCode>{char_code.upper()}</CharCode>')
    if start_pos == -1:
        return None
    text = answer.text[start_pos:]
    text = text[:text.find('</Value>')]
    str_value = text[text.rfind('>')+1:].replace(',','.')
    return float(str_value)


print(f'курс евро : {currency_rates("eur")} руб.')
print(f'курс доллара : {currency_rates("USD")} руб.')

