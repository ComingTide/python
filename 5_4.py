src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

# вывести те элементы списка, значения которых больше предыдущего

for i in range(len(src)-1):
    if src[i] < src[i+1]:
        result.append(src[i+1])

print('Вывод цикла: ', result)

result_second = [j for i, j in zip(src, src[1:]) if j > i]
print('Вывод генератора: ', result_second)