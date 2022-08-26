import datetime


class Utc:
    TimeOfDay = {'00': 'Ночь', '01': 'Ночь', '02': 'Ночь',
                 '03': 'Ночь', '04': 'Ночь', '05': 'Ночь', '06': 'Утро',
                 '07': 'Утро', '08': 'Утро', '09': 'Утро', '10': 'Утро',
                 '11': 'Утро', '12': 'День', '13': 'День', '14': 'День', '15': 'День',
                 '16': 'День', '17': 'День', '18': 'Вечер', '19': 'Вечер', '20': 'Вечер',
                 '21': 'Вечер', '22': 'Вечер', '23': 'Вечер'}

    def __init__(self, hours: int):
        self.hours = hours
        self.td = datetime.timedelta(hours=self.hours)
        self.tz = datetime.timezone(self.td)
        self.tn = datetime.datetime.now(self.tz)
        self.hd = datetime.datetime.strftime(self.tn, "%H")

    def __str__(self):
        return f'{Utc.TimeOfDay[self.hd]}'


# Если я правильно понял задание

u1 = Utc(3)
print(u1)
# Вечер
