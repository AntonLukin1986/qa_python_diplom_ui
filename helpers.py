'''Вспомогательные инструменты.'''
import random
import string


def generate_name():
    '''Генерация имени.'''
    return ''.join(
        random.choices(string.ascii_lowercase, k=8)
    ).capitalize()


def generate_password():
    '''Генерация пароля.'''
    return ''.join(
        random.choices(string.digits + string.ascii_letters, k=8)
    )


def generate_email():
    '''Генерация email.'''
    prefix = random.choices(string.digits + string.ascii_lowercase, k=10)
    return ''.join(prefix) + '@mail.ru'


def get_user_data():
    '''Получение данных пользователя.'''
    return {
        'name': generate_name(),
        'password': generate_password(),
        'email': generate_email()
    }


def format_locator(locator, value):
    '''Отформатировать локатор элемента.'''
    method, pattern = locator
    return method, pattern.format(value)


if __name__ == '__main__':
    print(get_user_data())
