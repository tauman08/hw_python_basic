# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self):
        self.title = ''
    def draw(self):
        print("Start rendering")

class Pen(Stationery):
    def draw(self):
        print('start pen drawing')

class Pencil(Stationery):
    def draw(self):
        print('start pencil drawing')

class Handle(Stationery):
    def draw(self):
        print('start handle drawing')

s = Stationery()
s.draw()
p = Pen()
p.draw()
Pn = Pencil()
Pn.draw()
h = Handle()
h.draw()