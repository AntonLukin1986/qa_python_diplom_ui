'''Универсальные шаблоны локаторов.'''
PREF = '//'

A = 'a'
BUTTON = 'button'
DIV = 'div'
H1 = 'h1'
H2 = 'h2'
INPUT = 'input'
LABEL = 'label'
P = 'p'
UL = 'ul'

ATTRIBUTE = '[@{}="{}"]'
CONTAINS_CLASS = '[contains(@class, "{}")]'
TEXT = '[text()="{}"]'
UP = '/ancestor::{}'

BUTTON_TXT = PREF + BUTTON + TEXT
HEADER1_TXT = PREF + H1 + TEXT
HEADER2_TXT = PREF + H2 + TEXT
LABEL_TXT = PREF + LABEL + TEXT
LINK_TXT = PREF + A + TEXT
PARAG_TXT = PREF + P + TEXT

A_CONTAINS_CLS = PREF + A + CONTAINS_CLASS
DIV_CONTAINS_CLS = PREF + DIV + CONTAINS_CLASS
P_CONTAINS_CLS = PREF + P + CONTAINS_CLASS
UL_CONTAINS_CLS = PREF + UL + CONTAINS_CLASS

INPUT_ATTR = PREF + INPUT + ATTRIBUTE
LINK_ATTR = PREF + A + ATTRIBUTE
