cube_list = []      # список в котором будут содержаться кубы нечетных чисел и задание (а)
new_cube_list = []  # список в который будут складываться числа из задания (b)
all_sum = 0         # объявление переменной которая будте хранить числа для вывода суммы из (a) и (b)

# заполняем список значениями от 1 до 1000
for i in range(1, 1001, 2):
# записываем элемент i^3 при помощи .append в конец списка cube_list с шагом 2 до 1000
    cube_list.append(i ** 3)
# перебираем элементы внутри cube_list[], объявляем digit_sum = 0, для дальнейшего присвоения ей значения
for index, val in enumerate(cube_list):
    digit_sum = 0
    while val > 0:
        digit_sum += val % 10
        val //= 10
# sum_digits после записи в нее числа, делится на 7 без остатка
    if digit_sum % 7 == 0:
# передаем значение по [index] из cube_list и складываем в all_sum
        all_sum += cube_list[index]
print(all_sum)

for x in cube_list:
    new_cube_list.append(x + 17)
# обнуляем значение all_sum
all_sum = 0

for index, val in enumerate(new_cube_list):
    digit_sum = 0
    while val > 0:
        digit_sum += val % 10
        val //= 10
    if digit_sum % 7 == 0:
        all_sum += new_cube_list[index]
print(all_sum)
