from pypinyin import Style
from pypinyin.constants import PHRASES_DICT
from pypinyin.converter import DefaultConverter

dc = DefaultConverter()
def change_style(s):
    return dc.convert_style(None, s, Style.TONE3, None)

def merge_py(vs):
    return ' '.join(change_style(v[0]) for v in vs)

with open('dest.txt', 'w') as f:
    for k, vs in PHRASES_DICT.items():
        print(k, merge_py(vs), sep='\t', file=f)
