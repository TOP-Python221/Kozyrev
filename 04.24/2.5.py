a = input('Кодинаты по горизонтали(от a до n): ')
b = int(input('Кодинаты по вертикали(от 1 до 8): '))
c = input('Кодинаты по горизонтали(от a до n): ')
d = int(input('Кодинаты по вертикали(от 1 до 8): '))
if (ord(a)+b) % 2 == 0 and (ord(c) + d) % 2 == 0: 
    print('yes')
elif (ord(a) + b) %2 != 0 and (ord(c) + b) % 2 != 0:
    print('yes')   
else:
    print('No')