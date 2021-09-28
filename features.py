#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from vars import consts
from utils import fetch_form, analyse_html, not_empty

"""
step1
~~~~~~~~~~~~~~~~~~~
切割 codes
"""
def step_1():
  return list(filter(not_empty, consts['codes'].split(',')))

"""
step2
~~~~~~~~~~~~~~~~~~~~
提交 sequence_textarea 换取 orig_AA_sequence
"""
def step_2():
  form_data = {
    'sequence_textarea': consts["sequence_textarea"]
  }

  res = fetch_form('protein_2.cgi', form_data)
  page_text = res.text.replace('\n', '')
  orig_AA_sequence = analyse_html(page_text, 'orig_AA_sequence', 'textarea')
  orig_DNA_sequence = analyse_html(page_text, 'orig_DNA_sequence')
  return orig_AA_sequence, orig_DNA_sequence

"""
step3
~~~~~~~~~~~~~~~~~~~~~~
提交 orig_AA_sequence 和 code 得到替换过片段的 new_AA_sequence
"""
def step_3(code, orig_DNA_sequence, orig_AA_sequence):
  form_data = {
    'code': code,
    'orig_DNA_sequence': orig_DNA_sequence,
    'orig_AA_sequence': orig_AA_sequence,
    'chopped_DNA_sequence': consts["chopped_DNA_sequence"],
    'protocol': consts["protocol"]
  }

  res = fetch_form('protein_3.cgi', form_data)
  page_text = res.text.replace('\n', '')
  new_AA_sequence = analyse_html(page_text, 'new_AA_sequence', 'textarea')
  orig_DNA_sequence = analyse_html(page_text, 'orig_DNA_sequence')
  return new_AA_sequence, orig_DNA_sequence

"""
step4
~~~~~~~~~~~~~~~~~~~~~~
提交 new_AA_sequence 得到最终结果
"""
def step_4(code, orig_DNA_sequence, new_AA_sequence):
  form_data = {
    'orig_DNA_sequence': orig_DNA_sequence,
    'chopped_DNA_sequence': consts["chopped_DNA_sequence"],
    'new_AA_sequence': new_AA_sequence,
    'protocol': consts["protocol"],
    'min_Tm': consts["min_Tm"],
    'max_Tm': consts["max_Tm"],
    'min_GC': consts["min_GC"],
    'max_GC': consts["max_GC"],
    'min_length': consts["min_length"],
    'max_length': consts["max_length"],
    'min_5p_flank': consts["min_5p_flank"],
    'max_5p_flank': consts["max_5p_flank"],
    'min_3p_flank': consts["min_3p_flank"],
    'max_3p_flank': consts["max_3p_flank"],
    # delete it to cancel checked
    'ends_in_GC': consts["ends_in_GC"],
    # delete it to cancel checked
    'mut_at_center': consts["mut_at_center"],
    'primer_type': consts["primer_type"],
    'species': consts["species"]
  }
  res = fetch_form('protein_4.cgi', form_data)

  reg = r'(<p />------------.*?###########<p />)'
  reg_text = re.search(reg, res.text.replace('\n', '')).group(1)

  reg_text = reg_text.replace('<p />', '\n')
  reg_text = reg_text.replace('<br />', '\n')
  reg_text = reg_text.replace('&nbsp;', ' ')

  return 'code: F625V' + reg_text + '\n\n'
