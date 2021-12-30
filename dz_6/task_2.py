#*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.


def pars(str_line,dict_ip):
    str_line =str(str_line).strip()
    end_str = str_line.find('-')-1
    str_ip = str_line[0:end_str]
    dict_ip.setdefault(str_ip,0)
    dict_ip[str_ip] += 1




if __name__ == '__main__':
    dict_ip = {}
    with open('E:\course\GB\python\\basic python\\file\\nginx_logs.txt') as f:
        for line in f:
            pars(line,dict_ip)

    result_list = list(dict_ip.items())
    print(result_list)