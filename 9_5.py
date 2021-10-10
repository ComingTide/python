class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    print('Уникальная ручка')


class Pencil(Stationery):
    print('Уникальный карандаш')


class Handle(Stationery):
    print('Уникальный маркер')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()