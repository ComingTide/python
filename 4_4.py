import utils

# Заводим переменную с интересующими нас валютами, если такого значения нет, то возвращаем None
current_list = ['EUR', 'LSP', 'USD', 'GbP']

# Выводим значение каждого курса и дату по очереди
for i in range(0, len(current_list)):
    print('Курс ', '"' + current_list[i] + '"', ' равен: ', utils.currency_rates(current_list[i]))