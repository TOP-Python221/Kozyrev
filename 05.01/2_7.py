sm = 0
number = int(input('Введите число: '))
print(f'Введите {number} значения: ')
for i in range(1, number + 1):
    i = int(input()) 
    sm += i  
print(sm)     
