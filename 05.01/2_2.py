sm = 0
number = int(input('Введите число: '))
print(f'Введите {number} значения: ')
for i in range(1, number + 1):
    i = int(input())
    if i > 0: 
        sm += i  
print(sm)     
