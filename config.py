'''Конфигурация тестов.'''


class Resolution:
    FHD = 1920, 1080


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

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
ORDER_HISTORY_PAGE = MAIN_PAGE + 'account/order-history'
API_CREATE_USER = MAIN_PAGE + 'api/auth/register'
API_DELETE_USER = MAIN_PAGE + 'api/auth/user'
