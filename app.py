#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fetch DNA code
~~~~~~~~~~~~~~~~~~~~

批量提交 code 解析 DNA 序列
使用的对象网站：http://bioinformatics.org/primerx/cgi-bin/protein_1.cgi
"""
from features import step_1, step_2, step_3, step_4
from utils import not_empty


code_list = step_1()
print("start select orig_AA_sequence...")
orig_AA_sequence, orig_DNA_sequence = step_2()
print("finish select orig_AA_sequence!")
write_text = ''

for code in code_list:
  print("start select code: " + code + ' ...')
  new_AA_sequence, orig_DNA_sequence = step_3(code, orig_DNA_sequence, orig_AA_sequence)
  result = step_4(code, orig_DNA_sequence, new_AA_sequence)
  write_text += result
  print("finish select code: " + code)

if not_empty(write_text):
  f = open('./result.txt', 'w')
  f.write(write_text)
  f.close()
  print("finish all select, please read result.txt")
