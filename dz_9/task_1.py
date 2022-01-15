# Создать класс TrafficLight (светофор)
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
#     второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
import itertools

class TrafficLight:
    def __init__(self):
        self.color = 'красный'
    def running(self):
        all_colors = ['красный','желтый','зеленый']
        for item in itertools.cycle(all_colors):
            self.color = item
            print(self.color)
            if item == 'красный':
                sleep(7)
            elif item == 'желтый':
                sleep(2)
            else:
                sleep(1)

a = TrafficLight()
a.running()