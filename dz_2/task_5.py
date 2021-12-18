# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать,
# что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

my_list = [57.8, 46.51, 97, 14500,105.23,87.15,520,248.56,111.50,52369]
str_finish = ''
count_price = len(my_list)
splitter = ','
id_before = id(my_list)


for idx,price in enumerate(my_list):
    if idx == count_price-1:
        splitter = ''
    if type(price) == int:
        str_finish += f'{price} руб 00 коп{splitter}'
    else:
        str_price = str(price)
        str_penny = str_price[:str_price.rfind("."):-1]
        if len(str_penny) == 1:
            str_penny += '0'
        str_rub = str_price[:str_price.find('.')]
        str_finish += f'{str_rub} руб {str_penny} коп{splitter}'

print(str_finish)
# B
print(f' ид списка до сортировки: {id_before}')
my_list.sort()
id_after = id(my_list)
print(f' ид списка после сортировки: {id_after}')

if id_before == id_after:
    print('Объект списка не изменился')
for price in my_list:
    print(price)
# C
sort_list = my_list.copy()
sort_list.sort(reverse=True)
print(sort_list)
print('Пять самых дорогих товаров:')
for price in sort_list[:5]:
    print(price)


