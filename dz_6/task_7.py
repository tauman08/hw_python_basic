import sys

if len(sys.argv) < 3:
    exit('Неверное количество аргументов')

with open('bakery.cav','r') as f:
    num_line = int(sys.argv[1])
    count_line = sum(1 for _ in f)
    if num_line > count_line:
        exit('Неверно указан номер строки файла')
    f.seek(0)

    with open('buffer.cav','w') as f_buffer:
        for i, line in enumerate(f):
            if (i+1) == num_line:
                f_buffer.write(sys.argv[2]+'\n')
            else:
                f_buffer.write(line)
with open('buffer.cav','r') as f_buffer:
    with open('bakery.cav','w') as f:
        for line in f_buffer:
                f.write(line)