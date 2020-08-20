import json
from pypinyin import Style
from pypinyin.constants import PINYIN_DICT
from pypinyin.converter import DefaultConverter

dc = DefaultConverter()
def change_style(s):
    '''
    >>> change_style('hán')
    'han2'
    '''
    return dc.convert_style(None, s, Style.TONE3, None)

def remove_tone(s):
    for d in '12345':
        s = s.replace(d, '')
    return s

largest_dict = {chr(k): [change_style(v) for v in vx.split(',')] for k, vx in PINYIN_DICT.items()}

with open('kHanyuPinlu.json') as f:
    d_hanyupinlu_x = {item['char']: {change_style(x['phonetic']): x['frequency'] for x in item['kHanyuPinlu']} for item in json.load(f)}

# For characters like 蔗.
# 蔗 has no tone in kHanyuPinlu. However, for the single character 蔗, we expect it to have a tone.
# Therefore, we delete 蔗 from d_hanyupinlu as if it does not exist, so the program will not process it.
d_hanyupinlu = {k: d for k, d in d_hanyupinlu_x.items() if not all(not s.endswith(tuple('1234')) for s in d)}

with open('dict.full') as f, open('dest.txt', 'w') as g:
    for line in f:
        ch, *vs = line.rstrip('\n').split(' ')

        if len(ch) != 1:
            continue  # single character only

        for v in vs:
            if ':' in v:  # has initial frequency
                v, freq = v.split(':')
                for py in largest_dict[ch]:
                    if ch not in d_hanyupinlu or py in d_hanyupinlu[ch]:
                        if remove_tone(py) == v:
                            print(ch, py, freq, sep='\t', file=g)  # use initial frequency
                    elif py not in d_hanyupinlu[ch]:
                        print(ch, py, '0%', sep='\t', file=g)  # rare pronunciation, assign 0%
            else:
                for py in largest_dict[ch]:
                    if ch not in d_hanyupinlu or py in d_hanyupinlu[ch]:
                        if remove_tone(py) == v:
                            print(ch, py, sep='\t', file=g)  # no frequency data
                    elif py not in d_hanyupinlu[ch]:
                        print(ch, py, '0%', sep='\t', file=g)  # rare pronunciation, assign 0%
