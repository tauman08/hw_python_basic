from utils import currency_rates

rate = currency_rates('eur')
print(f'Курс EUR на дату: {rate["date_rate"]} = {rate["value_rate"]} руб.')

rate = currency_rates('USD')
print(f'Курс USD на дату: {rate["date_rate"]} = {rate["value_rate"]} руб.')
