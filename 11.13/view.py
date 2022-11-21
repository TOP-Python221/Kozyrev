""" Модуль CLI - представления"""


def start_view():
    print('Добро пожаловать!!!')


def exit_answer():
    print('Для выхода оставьте поля пустым и нажмите ENTER')


def answer_view():
    return input('Введите ваш email --> ')


def show_result():
    print('Ваш Email сохранен')


def no_valid_email():
    print('-->Ваш email нам подходит! Попробуйте еще раз.<--')


def end_view():
    print('До скорых встреч')