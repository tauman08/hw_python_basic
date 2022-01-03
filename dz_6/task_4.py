
f_name = open('ФИО.csv',encoding='utf-8')
f_hobby = open('хобби.csv',encoding='utf-8')
f_result = open('users_hobby.txt','w+',encoding='utf-8')

count_name = sum(1 for _ in f_name)
count_hobby = sum(1 for _ in f_hobby)
f_hobby.seek(0)
f_name.seek(0)
if count_name < count_hobby:
    print('1')
else:
    for i, line in enumerate(f_name):
        if (i+1) <= count_hobby:
            f_result.write(line.strip()+': '+f_hobby.readline().strip()+'\n')
        else:
            f_result.write(line.strip() + ': None\n')


