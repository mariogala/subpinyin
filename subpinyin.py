#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
subpinyin.py
Script to add pinyin subtitles to Chinese characters
https://github.com/mariogala/subpinyin

Copyright (C) 2020  Mario Gala

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
import sys

from cjklib import characterlookup


# Maps the romanisation command line argument to the (reading,toneMarkType)
# params of CharacterLookup.getReadingForCharacter()
rom_param_map = {
    'Pinyin': ('Pinyin', 'diacritics'),
    'PinyinNum': ('Pinyin', 'numbers'),
    'CantoneseYale': ('CantoneseYale', 'diacritics'),
    'CantoneseYaleNum': ('CantoneseYale', 'numbers'),
    'CantoneseJyutping': ('Jyutping', 'numbers'),
}

CharLookup = characterlookup.CharacterLookup('C')

def subtitle_line(line, romanisation):
    """
    Subtitles the given line of Chinese text using the given romanisation.
    Returns a tuple where the first element is the list of Chinese characters
    and the second element is the list of corresponding romanisations.
    """
    if len(line)<=0:
        return None
    zh_chars = []
    rom_chars = []
    for ch in line:
        param = rom_param_map[romanisation]
        rom = CharLookup.getReadingForCharacter(ch, param[0], toneMarkType=param[1])
        zh_chars.append(ch)
        rom_chars.append(rom)
    return (zh_chars, rom_chars)

def output_line_tab(zh_chars, rom_chars):
    """
    Convert the given lines of Chinese characters and subtitles into tab-separated strings.
    """
    zh_out_str = '\t'.join(zh_chars)
    rom_out_str = '\t'.join(['/'.join(r) for r in rom_chars])
    return (zh_out_str, rom_out_str)

def main():
    parser = argparse.ArgumentParser(description='Add pinyin subtitles to Chinese characters.')
    parser.add_argument('-r', '--romanisation', '--romanization',
        default='Pinyin',
        choices=rom_param_map.keys(),
        help='Romanisation to use',
    )
    args = parser.parse_args()

    for input_line in sys.stdin:
        input_line = input_line.strip('\n\r').decode('utf-8')
        (zh_chars, rom_chars) = subtitle_line(input_line, args.romanisation)
        (zh_out_str, rom_out_str) = output_line_tab(zh_chars, rom_chars)
        print zh_out_str
        print rom_out_str

if __name__ == "__main__":
    main()
