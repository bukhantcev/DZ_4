# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого
# куста есть ровно два соседних. Всего на грядке растет N кустов.
# Семинар 4 2
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

from random import randint as ri
n_kustov = int(input("Vvedite kolichestvo kustov: "))
arr_urogainost = [ri(0, 70) for _ in range(n_kustov)]

print(arr_urogainost)
result = 0
for i in range(len(arr_urogainost) - 1):
    i *= -1
    if arr_urogainost[i - 1] + arr_urogainost[i] + arr_urogainost[i + 1] > result:
        result = arr_urogainost[i - 1] + arr_urogainost[i] + arr_urogainost[i + 1]
for i in range(len(arr_urogainost) - 1):
    if arr_urogainost[i - 1] + arr_urogainost[i] + arr_urogainost[i + 1] > result:
        result = arr_urogainost[i - 1] + arr_urogainost[i] + arr_urogainost[i + 1]
print(result)

