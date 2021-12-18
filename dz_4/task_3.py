#*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import requests
import datetime as dt

def currency_rates(char_code):
    answer =  requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if answer.ok == False:
        return None

    res = {'date_rate':None,'value_rate':None}
    str_date = answer.text[answer.text.find('Date="')+6:answer.text.find('" name=')]
    res['date_rate'] = dt.date(int(str_date[6:]),int(str_date[4:5]),int(str_date[:2]))

    start_pos = answer.text.find(f'<CharCode>{char_code.upper()}</CharCode>')
    if start_pos == -1:
        return None

    text = answer.text[start_pos:]
    text = text[:text.find('</Value>')]
    str_value = text[text.rfind('>')+1:].replace(',','.')
    res['value_rate'] = float(str_value)
    return res

rate = currency_rates('eur')
print(f'Курс EUR на дату: {rate["date_rate"]} = {rate["value_rate"]} руб.')
