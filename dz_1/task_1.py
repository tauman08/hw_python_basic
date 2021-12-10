# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите промежуток времени в сек.: '))
fix_interval = [[86400,' дн '],[3600,' час '],[60,' мин '],[1,' сек ']]
result_interval = []
for interval in fix_interval:
    if duration == 0:
        break
    if duration >= interval[0]:
        duration_interval = duration // interval[0]
        result_interval.append([duration_interval,interval[1]])
        duration = duration % interval[0]

if len(result_interval) == 0:
    str_result = 'Введен нулевой интервал. '
else:
    str_result = ''
    for interval in result_interval:
        str_result = str_result + str(interval[0]) + interval[1]

print(str_result)

