# subpinyin
Script to add pinyin subtitles to Chinese characters

## Requirements
* Python 2.4+
* Cjklib: https://github.com/cburgmer/cjklib

## Usage
The Chinese text is read from standard input, line by line.

For each line, the script then writes to standard output:
* the original line of Chinese text, with tabs separating the characters;
* the line of pinyin subtitles, also tab-separated.

For Chinese characters that have more than one romanisation, all the romanisations are included, separated by slash.

### Parameters
```
-r, --romanisation, --romanization
    Romanisation to use in the output
        Pinyin (default): Hanyu Pinyin, using accents as tone marks
        PinyinNum: Hanyu Pinyin, using numbers as tone marks
        CantoneseYale: Cantonese Yale, using accents as tone marks
        CantoneseYaleNum: Cantonese Yale, using numbers as tone marks
        CantoneseJyutping: Cantonese Jyutping
```

### Examples

#### Mandarin Hanyu Pinyin
```
$ echo "你好" | ./subpinyin.py
你	好
nǐ	hāo/hǎo/hào
```

#### Cantonese
```
$ echo "今天我 寒夜裡看雪飄過" | ./subpinyin.py --romanisation=CantoneseYaleNum
今	天	我	 	寒	夜	裡	看	雪	飄	過
gam1	tin1	ngo5		hon4	ye6	lei5/leui5	hon1/hon3	syut3	piu1	gwo1/gwo3
```

```
$ echo "今天我 寒夜裡看雪飄過" | ./subpinyin.py --romanisation=CantoneseYale
今	天	我	 	寒	夜	裡	看	雪	飄	過
gām	tīn	ngóh		hòhn	yeh	léih/léuih	hōn/hon	syut	pīu	gwō/gwo
```

```
$ echo "今天我 寒夜裡看雪飄過" | ./subpinyin.py --romanisation=CantoneseJyutping
今	天	我	 	寒	夜	裡	看	雪	飄	過
gam1	tin1	ngo5		hon4	je6	lei5/leoi5	hon1/hon3	syut3	piu1	gwo1/gwo3
```
