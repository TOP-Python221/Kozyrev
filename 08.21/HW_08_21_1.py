import math


class Tetrahedron:
    def __init__(self, length_A: int):
        self.length_A = length_A
        self.square = self.length_A ** 2 * math.sqrt(3)
        self.volume = math.sqrt(2) * self.length_A ** 3 / 12

    def __str__(self):
        return f'Площадь правильного тетраэдра = {self.square}\n' \
               f'Объем правильного тетраэдра = {self.volume}'


t1 = Tetrahedron(30)
print(t1)

# Площадь правильного тетраэдра = 5050.660154870846
# Объем правильного тетраэдра = 18557.310365459754
