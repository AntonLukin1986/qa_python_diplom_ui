'''Конфигурация тестов.'''


class Url:
    MAIN = 'https://stellarburgers.nomoreparties.site/'
    ORDER_HISTORY = MAIN + 'account/order-history'
    CREATE_USER = MAIN + 'api/auth/register'
    DELETE_USER = MAIN + 'api/auth/user'


class Resolution:
    FHD = 1920, 1080
    QHD = 2560, 1440


BROWSERS = {
    'Chrome': ['--window-size={},{}'.format(*Resolution.FHD)],
    'Firefox': '--width={} --height={}'.format(*Resolution.FHD).split()
}

FIREFOX_JS = '''
function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
    var dataTransfer = new DataTransfer();
    var dragStartEvent = new DragEvent(
        'dragstart',
        {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    sourceNode.dispatchEvent(dragStartEvent);
    var dropEvent = new DragEvent(
        'drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    destinationNode.dispatchEvent(dropEvent);
    var dragEndEvent = new DragEvent(
        'dragend',
        {bubbles: true, cancelable: true, dataTransfer: dataTransfer}
    );
    sourceNode.dispatchEvent(dragEndEvent);
}
simulateHTML5DragAndDrop(arguments[0], arguments[1]);
'''
