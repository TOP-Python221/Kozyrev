Numbertime = input('Введите величину временного интервала в минутах: ')
hours = str(int(Numbertime) // 60)
minuts = str(int(Numbertime) % 60 )
if int(hours)<=1:
    print(Numbertime + ' мин - это ' + hours +' час ' + minuts+' мин')
else:
    print(Numbertime + ' мин - это ' + hours +' часa ' + minuts+' мин')