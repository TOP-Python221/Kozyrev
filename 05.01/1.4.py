a = ord(input('Кодинаты по горизонтали(от a до h): '))
b = int(input('Кодинаты по вертикали(от 1 до 8): '))
c = ord(input('Кодинаты по горизонтали(от a до h): '))
d = int(input('Кодинаты по вертикали(от 1 до 8): '))
if (a - c != 1) and (b - d != 1):
    print("Нет")
else:
    print("Да")    