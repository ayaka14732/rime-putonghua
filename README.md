# rime-putonghua

**kfcd**

来自[开放词典](http://kaifangcidian.com/)。

```sh
cd kfcd
wget http://kaifangcidian.com/xiazai/cidian_zhzh-kfcd.zip
unzip cidian_zhzh-kfcd.zip
python build.py
cd ..
```

**cs**

参考了搜狗输入法的四个计算机词库：OI算法、信息学奥林匹克联赛常用算法和数据结构、开发大神专用词库、计算机名词，使用 [pypinyin](https://pypinyin.readthedocs.io/) 标注拼音，并人工校对。

```sh
cd cs
wget https://github.com/studyzy/imewlconverter/releases/download/v2.9.0/imewlconverter_Linux_Mac.tar.gz
tar -zxvf imewlconverter_Linux_Mac.tar.gz
wget https://pinyin.sogou.com/d/dict/download_cell.php?id=96142&name=OI%E7%AE%97%E6%B3%95 -O OI算法.scel
wget https://pinyin.sogou.com/d/dict/download_cell.php?id=76904&name=%E4%BF%A1%E6%81%AF%E5%AD%A6%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%81%94%E8%B5%9B%E5%B8%B8%E7%94%A8%E7%AE%97%E6%B3%95%E5%92%8C%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84 -O 信息学奥林匹克联赛常用算法和数据结构.scel
wget http://download.pinyin.sogou.com/dict/download_cell.php?id=75228&name=%E5%BC%80%E5%8F%91%E5%A4%A7%E7%A5%9E%E4%B8%93%E7%94%A8%E8%AF%8D%E5%BA%93%E3%80%90%E5%AE%98%E6%96%B9%E6%8E%A8%E8%8D%90%E3%80%91 -O 开发大神专用词库.scel
wget http://download.pinyin.sogou.com/dict/download_cell.php?id=151&name=%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%90%8D%E8%AF%8D -O 计算机名词.scel
dotnet ImeWlConverterCmd.dll -i:scel OI算法.scel -o:rime OI算法.txt
dotnet ImeWlConverterCmd.dll -i:scel 信息学奥林匹克联赛常用算法和数据结构.scel -o:rime 信息学奥林匹克联赛常用算法和数据结构.txt
dotnet ImeWlConverterCmd.dll -i:scel 开发大神专用词库.scel -o:rime 开发大神专用词库.txt
dotnet ImeWlConverterCmd.dll -i:scel 计算机名词.scel -o:rime 计算机名词.txt
python build.py
cd ..
```

**pypinyin**

由 pypinyin 直接导出的词库。

```sh
cd pypinyin
python build.py
cd ..
```

**places**

参考了搜狗输入法的两个地名词库：全国省市区县地名大全、行政地区，使用 pypinyin 标注拼音，并人工校对。

```sh
cd places
wget https://pinyin.sogou.com/d/dict/download_cell.php\?id\=52622\&name\=%E5%85%A8%E5%9B%BD%E7%9C%81%E5%B8%82%E5%8C%BA%E5%8E%BF%E5%9C%B0%E5%90%8D%E5%A4%A7%E5%85%A8\&f\=detail -O 全国省市区县地名大全.scel
wget https://pinyin.sogou.com/d/dict/download_cell.php\?id\=204\&name\=%E8%A1%8C%E6%94%BF%E5%9C%B0%E5%8C%BA\&f\=detail -O 行政地区.scel
dotnet ../cs/ImeWlConverterCmd.dll -i:scel 全国省市区县地名大全.scel -o:rime 全国省市区县地名大全.txt 
dotnet ../cs/ImeWlConverterCmd.dll -i:scel 行政地区.scel -o:rime 行政地区.txt 
python build.py
cd ..
```

**places2**

手工录入的地名词库。

**liuxingyu**

参考了维基百科《[中国大陆网络用语列表](https://zh.wikipedia.org/zh-cn/中国大陆网络用语列表)》，使用 pypinyin 标注拼音，并人工校对。

```sh
cd liuxingyu
wget https://zh.wikipedia.org/zh-cn/中国大陆网络用语列表 -O 中国大陆网络用语列表.html
python build.py
cd ..
```

**sunpinyin**

参考了 sunpinyin，使用 pypinyin 标注拼音。

```sh
cd sunpinyin
wget https://raw.githubusercontent.com/sunpinyin/open-gram/master/data/dict.full
python build.py
cd ..
```

**sunpinyin2**

参考了 sunpinyin，手工标注拼音。

**char**

由 pypinyin 直接导出，参考了 sunpinyin 及 Unihan 数据库。

```sh
cd char
unihan-etl -F json -f kHanyuPinlu -d ./kHanyuPinlu.json
cp ../sunpinyin/dict.full .
python build.py
cd ..
```

**cedict**

来自 [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict)。

```sh
cd cedict
wget https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz
gunzip cedict_1_0_ts_utf-8_mdbg.txt.gz
python build.py
cd ..
```
