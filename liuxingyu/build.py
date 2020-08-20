from bs4 import BeautifulSoup
import re
from pypinyin import lazy_pinyin, Style

# https://ayaka.shn.hk/hanregex/
# 〇 本来也是汉字，但萌百中用作占位符，如 〇还是个孩子，故去掉
han_symbols_regex = re.compile(r'^[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\U0002ceb0-\U0002ebef\U00030000-\U0003134f，·：]+$')
def is_han_string(s):
    return bool(han_symbols_regex.match(s))

def is_valid_string(s):
    return len(s) > 1 and is_han_string(s)

with open('中国大陆网络用语列表.html') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'lxml')
items = [match[1] for li in soup.select('#bodyContent li') for match in (re.match(r'^([^：]+?)：', li.text),) if match]

def get_pinyin(s):
    return ' '.join(py for py in lazy_pinyin(s, style=Style.TONE3) if not re.match(r'^[ ，·：]+$', py))

data = sorted(((y, get_pinyin(y)) for item in items for x in item.split('/') for y in x.split('、') if is_valid_string(y)), key=lambda a_b: (len(a_b[0]), a_b[1], a_b[0]))

with open('dest.txt', 'w') as f:
    for ch, py in data:
        print(ch, py, sep='\t', file=f)
