from itertools import chain
from pypinyin import lazy_pinyin, Style

def get_pinyin(s):
    return ' '.join(lazy_pinyin(s, style=Style.TONE3))

def remove_tones(s):
    for digit in '1234':
        s = s.replace(digit, '')
    return s

d = {}

with open('行政地区.txt') as f1, open('全国省市区县地名大全.txt') as f2:
    for line in chain(f1, f2):
        ch, _, _ = line.rstrip('\n').split('\t')
        d[ch] = get_pinyin(ch)

with open('manual_fix.txt') as f:
    d_manual_fix = {k: v for line in f for k, v in (line.rstrip().split('\t'),)}

d = {**d, **d_manual_fix}

with open('dest.txt', 'w') as f:
    for ch, py in d.items():
        print(ch, py, sep='\t', file=f)
