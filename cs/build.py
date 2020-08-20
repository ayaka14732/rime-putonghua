from itertools import chain
from pypinyin import lazy_pinyin, Style

def get_pinyin(s):
    return ' '.join(lazy_pinyin(s, style=Style.TONE3))

def remove_tones(s):
    for digit in '1234':
        s = s.replace(digit, '')
    return s

d = {}

with open('OI算法.txt') as f1, open('信息学奥林匹克联赛常用算法和数据结构.txt') as f2, open('开发大神专用词库.txt') as f3, open('计算机名词.txt') as f4:
    for line in chain(f1, f2, f3, f4):
        ch, _, _ = line.rstrip('\n').split('\t')
        d[ch] = get_pinyin(ch)

with open('manual_fix.txt') as f:
    d_manual_fix = {k: v for line in f for k, v in (line.rstrip().split('\t'),)}

d = {**d, **d_manual_fix}

with open('dest.txt', 'w') as f:
    for ch, py in d.items():
        print(ch, py, sep='\t', file=f)
