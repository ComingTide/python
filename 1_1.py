duration = int(input("Введите секунды: "))
sec = duration % (24 * 86400)
day = sec // 86400
sec %= 86400
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print("В {} секундах".format(duration))
print ("{} дн. {} час. {} мин. {} сек.".format(day,hour,min,sec))