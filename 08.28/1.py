"""Представление матрицы с обычными атрибутами"""

class Matrix:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        self.show_elem = '\n'.join([
            '\t'.join([str(j) for j in i])
            for i in self.elem
        ])
        return self.show_elem

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.elem)):
            for j in range(len(self.elem[i])):
                summa = other.elem[i][j] + self.elem[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.elem):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __sub__(self, other_sub):
        result_sub = []
        numbers = []
        for i in range(len(self.elem)):
            for j in range(len(self.elem[i])):
                summa = other_sub.elem[i][j] - self.elem[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.elem):
                    result_sub.append(numbers)
                    numbers = []
        return Matrix(result_sub)


g = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 5, 3, 66]]
a = [[5, 25, 35, 45], [57, 66, 75, 84], [15, 56, 37, -24]]

m1 = Matrix(g)
m2 = Matrix(a)
m3 = m1 + m2
m4 = m2 - m1
print(m3)
print(m4)


# stdout +
# 6	 27	38
# 49 62	72
# 82 92	16
# 61 40	42

# stdout -
# -4 -23 -32
# -41 -52 -60
# -68 -76 -14
# -51 -34 90
