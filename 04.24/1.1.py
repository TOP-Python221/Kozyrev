import datetime
Firstname = input('Введите своё имя: ')
Lastname = input('Введите свою фамилию: ')
Dateofbirth = input('Введите год своего рождения: ')
time = datetime.date.today()
Years = int(time.year) - int(Dateofbirth)

print(Firstname, Lastname + ', ' + str(Years))