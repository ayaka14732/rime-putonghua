import re

# https://ayaka.shn.hk/hanregex/
# 〇 本来也是汉字，但萌百中用作占位符，如 〇还是个孩子，故去掉
han_symbols_regex = re.compile(r'^[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\U0002ceb0-\U0002ebef\U00030000-\U0003134f，·：]+$')
def is_han_string(s):
    return bool(han_symbols_regex.match(s))

def is_valid_string(s):
    return len(s) > 1 and is_han_string(s)

def regularize_py(s):
    s = s.lower()
    s = s.replace('u:', 'v')  # 女 nu: -> nv
    s = re.sub(r'\br\b', 'er', s)  # 儿 r -> er
    return s

def parse_cedict_line(line):
    '''Parse one line of the CC-CEDICT and return (word, pinyin) pair'''
    l, r, *_ = line.split('[')
    py = r.split(']')[0]
    w = l.split(' ')[1]
    return w, py

s = set()

with open('cedict_1_0_ts_utf-8_mdbg.txt') as f:
    for line in f:
        line = line.rstrip()

        if line[0] == '#':
            continue  # ignore comments

        ch, py = parse_cedict_line(line)
        py = regularize_py(py)
        if is_valid_string(ch):
            s.add((ch, py))

l = sorted(s, key=lambda xy: (xy[1], xy[0]))

with open('dest.txt', 'w') as f:
    for ch, py in l:
        print(ch, py, file=f, sep='\t')
