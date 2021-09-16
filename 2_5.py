# random list of prices was created
price = [57.8, 46.51, 97, 88.44, 32.03, 2, 232.57, 10.08, 12.07, 28.11, 99, 4421.32, 65.5, 6, 765.65, 32.01, 32.02]
# for the convenience of separation, we use the text of the exercise
print(f"\n A) - Вывести на экран эти цены через запятую в одну строку, "
      f"цена должна отображаться в виде <r> руб <kk> коп\n")
# return the values of rub and kop, add "0" to two integer digits
for n in price:
    rub, kop = str(f"{n:.2f}").split(".")
    print(f"{rub} руб. {int(kop):02d} коп., ", end=" ")

print(f"\n\n B) - Вывести цены, отсортированные по возрастанию, новый список не создавать\n")
# return the id of the memory cell, for sorting - .sort()
print(f"ID first_list:- {id(price)} - {price}")
price.sort()
print((f"ID new_list:- {id (price)} - {price}"))

print(f"\n C) - Создать новый список, содержащий те же цены, но отсортированные по убыванию \n")
# return the id of the memory cell, sorted - reverse
new_list = sorted(price, reverse=True)
print(f"ID new_list:- {id(new_list)} - {new_list}")

print(f"\n D) - Вывести цены пяти самых дорогих товаров. "
      f"Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?\n")
# returns a sorted list, output the last 5 indexes - [:5], flip - [::-1]
print(f"{new_list[0:5][::-1]}")