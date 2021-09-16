# in staff added initial list
staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# iterate over the data from the list and bring them to a general form
for n in staff:
    print((f"Привет, {n.split()[-1].title()}! Хорошего рабочего дня!"))
