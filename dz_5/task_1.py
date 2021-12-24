#Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

def nums_gen(n):
    for num in range(1,n+1,2):
        yield num

print(*nums_gen(20))

# задача 2
#*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def gen2(n):
    num_gens2 = (num for num in range(1,n+1,2))
    return num_gens2

print(*gen2(20))


