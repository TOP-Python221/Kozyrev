years = int(input('Введите свой возраст, а я скажу вам к какой возрастной группе вы относитесь: '))
if years<=13:
    print('Вы еще ребенок')
elif years>=14 and years<=24:
    print('Молодой')
elif years>=25 and years<=59:
    print('Зрелый') 
else:
    print('Старость')