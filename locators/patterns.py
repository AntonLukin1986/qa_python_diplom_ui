'''Универсальные шаблоны локаторов.'''                          # зауниверсалить!!1
CONTAINS_CLASS = '[contains(@class, "{}")]'
TEXT = '[text()="{}"]'
ATTRIBUTE = '[@{}="{}"]'

BUTTON_TXT = '//button' + TEXT
HEADER_TXT = '//h2' + TEXT
LABEL_TXT = '//label' + TEXT
LINK_TXT = '//a' + TEXT
PARAGRAPH_TXT = '//p' + TEXT

DIV_CONTAINS_CLS = '//div' + CONTAINS_CLASS

INPUT_ATTR = '//input' + ATTRIBUTE
LINK_ATTR = '//a' + ATTRIBUTE
