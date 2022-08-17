number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
if number1==0 or number2==0:
    print('Числа должны быть целые не равные нулю!')
elif number1 % number2 == 0:
    print(f'{number1} делится на {number2} нацело')
    print(f'Частное: {int(number1/number2)}')
elif number1 % number2 >0:
    print(f'{number1} не делится на {number2} нацело')
    print(f'Частное: {int(number1/number2)}')
    print(f'Остаток: {int(number1%number2)}')
