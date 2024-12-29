'''Конфигурация тестов.'''
FHD = 1920, 1080

BROWSERS = {
    'Chrome': ['--window-size={},{}'.format(*FHD)],
    # 'Firefox': '--width={} --height={}'.format(*FHD).split()
}

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
API_CREATE_USER = MAIN_PAGE + 'api/auth/register'
API_DELETE_USER = MAIN_PAGE + 'api/auth/user'
