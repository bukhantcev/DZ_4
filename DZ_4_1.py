# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint as ri

len_1 = int(input("Введите кщличество элементов первого множества: "))
len_2 = int(input("Введите кщличество элементов второго множества: "))

first_list = [ri(0, ri(0, 100)) for _ in range(len_1)]
second_list = [ri(0, ri(0, 100)) for _ in range(len_2)]
print(f"Первое множество: {first_list}")
print(f"Второе множество: {second_list}")
final_list = list(set(first_list + second_list))
print(f"Объединенное неупорядоченное множество: {final_list}")
result = []
for i in range(len(final_list)-1):
    for k in range(i, len(final_list)):
        if final_list[i] > final_list[k]:
            final_list[i], final_list[k] = final_list[k], final_list[i]
print(f"Ответ: {final_list}")







