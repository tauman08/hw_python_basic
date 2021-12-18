from utils import currency_rates
import sys

rate = currency_rates(sys.argv[1])
print(f'{rate["value_rate"]}, {rate["date_rate"]}')

