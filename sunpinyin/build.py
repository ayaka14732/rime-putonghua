from itertools import chain
from pypinyin import lazy_pinyin, Style

def get_pinyin(s):
    return ' '.join(lazy_pinyin(s, style=Style.TONE3))

def remove_tones(s):
    for digit in '1234':
        s = s.replace(digit, '')
    return s

d = {}

with open('dict.full') as f:
    for line in f:
        s, py_orig, *_ = line.rstrip('\n').split(' ')
        if len(s) > 1:
            py = get_pinyin(s)
            if py_orig.replace("'", ' ') == remove_tones(py):
                d[s, py] = None

with open('dest.txt', 'w') as f:
    for ch, py in d:
        print(ch, py, sep='\t', file=f)
