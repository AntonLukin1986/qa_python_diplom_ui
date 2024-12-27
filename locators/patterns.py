'''Универсальные шаблоны локаторов.'''
CONTAINS_CLASS = '[contains(@class, "{}")]'
TEXT = '[text()="{}"]'

BUTTON_TXT = '//button' + TEXT
HEADER_TXT = '//h2' + TEXT
LABEL_TXT = '//label' + TEXT
LINK_TXT = '//a' + TEXT

DIV_CONTAINS_CLS = '//div' + CONTAINS_CLASS
