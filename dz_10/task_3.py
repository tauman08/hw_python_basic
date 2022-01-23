class Cell:
    def __init__(self,count):
        self.count = count

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError('Операция доступна только между операндами класса Cell')
        return Cell(self.count+other.count)
    def __sub__(self, other):
        if type(other) != type(self):
            raise TypeError('Операция доступна только между операндами класса Cell')
        difference = self.count - other.count
        if difference <= 0:
            raise ValueError('Результат не может быть меньше 1')
        return Cell(difference)
    def __mul__(self, other):
        if type(other) != type(self):
            raise TypeError('Операция доступна только между операндами класса Cell')
        return Cell(self.count*other.count)

    def __truediv__(self, other):
        if type(other) != type(self):
            raise TypeError('Операция доступна только между операндами класса Cell')
        return Cell(self.count/other.count)

    def make_order(self,count_in_line):
        return '\n'.join(['*'*count_in_line for _ in range(self.count//count_in_line)])\
                + '\n' + '*'*(self.count%count_in_line)

a = Cell(10)
b = Cell(15)
c = a + b
print(c.count)
print(c.make_order(6))