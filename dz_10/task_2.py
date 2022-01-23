from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,name,param):
        self.name   = name
        self.param  = param

    @abstractmethod
    def calc_consumption(self):
        pass

class Coat(Clothes):
    @property
    def calc_consumption(self):
        return round(self.param/6.5+0.5)

class Costum(Clothes):
    @property
    def calc_consumption(self):
        return round(self.param*2+0.3)

coat = Coat('Осеннее пальто',52)
print(coat.calc_consumption)
costum = Costum('Деловой костюм',1.75)
print(f'Расход ткани на {costum.name} составил {costum.calc_consumption} м')