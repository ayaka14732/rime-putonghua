import re

# https://ayaka.shn.hk/hanregex/
# 〇本来也是汉字，但萌百中用作占位符，如〇还是个孩子，故去掉
han_symbols_regex = re.compile(r'^[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\U0002ceb0-\U0002ebef\U00030000-\U0003134f，·：]+$')
def is_han_string(s):
    return bool(han_symbols_regex.match(s))

def is_valid_string(s):
    return len(s) > 1 and is_han_string(s)

with open('cidian_zhzh-kfcd-2019623.txt') as f, open('dest.txt', 'w') as g:
    for line in f:
        if line == '［繁體字］\t［簡體字］\t［漢語拼音］\n':
            next(f)
            break
    for line in f:
        _, b, c = line.split('\t')
        if is_valid_string(b):
            g.write(b + '\t' + c)
