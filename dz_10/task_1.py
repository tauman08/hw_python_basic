class ErrorDimension(BaseException):
    pass

class Matrix:
    def __init__(self,list_matrix):
        self.matrix = list_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str,line)) for line in self.matrix])

    def __add__(self, other):
        result_matrix = []
        if len(self.matrix) == len(other.matrix):
            for line1,line2 in zip(self.matrix,other.matrix):
                if len(line1) != len(line2):
                    raise ErrorDimension(f'Различное количество колонок в матрицах')
                result_matrix.append([x+y for x,y in zip(line1,line2)])
        else:
            raise ErrorDimension(f'Различное количество строк в матрицах')
        return Matrix(result_matrix)


a = Matrix([[1,2],[3,4]])
b = Matrix([[1,2],[3,4]])
c = a + b
print (c)