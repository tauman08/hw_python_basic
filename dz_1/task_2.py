# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
# операции! К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7. Решить задачу под пунктом b, не создавая новый список.

num_list = []
global_sum = 0
for num in range(1,1000,2):
    num_cube = num**3
    num_list.append(num_cube)
    str_num = str(num_cube)
    local_sum = 0
    for i in range(0,len(str_num)):
        local_sum += int(str_num[i])
    if local_sum % 7 == 0:
         global_sum += num_cube

print(num_list)
print(global_sum)

# вариант b без создания нового списка

global_sum = 0
index_list = 0
for num in num_list:
    num += 17
    num_list[index_list] = num
    index_list += 1

    str_num = str(num)
    local_sum = 0
    for i in range(0,len(str_num)):
        local_sum += int(str_num[i])
    if local_sum % 7 == 0:
        global_sum += num


print(num_list)
print(global_sum)

