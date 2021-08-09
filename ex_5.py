#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    title = "Pen"

    def draw(self):
        print(f'Я рисую {self.title}')

class Pencil(Stationary):
    title = "Pensil"

    def draw(self):
        print(f'Я рисую {self.title}')

class Handle(Stationary):
    title = "Handle"

    def draw(self):
        print(f'Я рисую {self.title}')

pen = Pen()
pensil = Pencil()
handle = Handle()
pen.draw()
pensil.draw()
handle.draw()
