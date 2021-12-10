# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:


for i in range(1,101):
    str_suffix = ''
    last_num = int(str(i)[-1])
    if  last_num > 1  and last_num < 5:
        str_suffix = 'а'
    elif last_num != 1:
        str_suffix = 'ов'
    print(i,'процент'+str_suffix)