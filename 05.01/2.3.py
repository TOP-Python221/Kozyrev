sm = 0
number = int(input('Введите число: '))
a = 1
for a in range(1, number + 1):
    if number % a == 0: 
        sm += a  
        ++a
print(sm)
    