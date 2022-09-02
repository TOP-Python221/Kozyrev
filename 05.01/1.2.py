yer = int(input("Введите год: "))
if yer % 4 == 0 and yer % 100 != 0 or yer % 400 == 0:
    print("Да")
else:
    print("Нет")    