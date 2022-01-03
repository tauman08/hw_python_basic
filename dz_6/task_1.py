# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
def parse(str_line):
    res_list = []
    str_line =str(str_line).strip()
    end_str = str_line.find('-')-1
    res_list.append(str_line[0:end_str])

    str_line = str_line[end_str:]
    start_str = str_line.find('"')+1
    str_line = str_line[start_str:]
    end_str = str_line.find(' ')
    res_list.append(str_line[:end_str])

    str_line = str_line[end_str:]
    start_str = str_line.find('/')
    str_line = str_line[start_str:]
    end_str = str_line.find('"')
    res_list.append(str_line[:end_str])

    return tuple(res_list)

if __name__ == '__main__':
    list_parse = []
    with open('E:\course\GB\python\\basic python\\file\\nginx_logs.txt') as f:
        for line in f:
            list_parse.append(parse(line))


    print(*list_parse)
