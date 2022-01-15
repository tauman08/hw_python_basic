# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'white'
        self.name = 'default-car-name'
        self.is_police = False
    def go(self):
        print(f'car {self.name} started moving ')
    def stop(self):
        print(f'car {self.name} stopped')
    def turn(self,direction = 'left'):
        print(f'car {self.name} tourn {direction}')
    def show_speed(self):
        print(f'speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'ALARM!!! Movement speed exceeded')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'ALARM!!! Movement speed exceeded')

class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True

car = TownCar()
car.name = 'FORD'
car.speed = 100
car.go()
car.turn('right')
car.show_speed()
car.stop()
