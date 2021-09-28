#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_toolbelt import MultipartEncoder
import requests
import re

def fetch_form(url, data):
  base_url = 'http://bioinformatics.org/primerx/cgi-bin/'
  form_data = MultipartEncoder(fields=data)
  return requests.post(base_url + url, data=form_data, headers={'Content-Type': form_data.content_type})

def analyse_html(text, name, type = 'input'):
  reg = '<input.*?name="' + name + '".*?value="(.*?)".*?/>'
  if type == 'textarea':
    reg = '<textarea name="' + name + '".*?>(.*?)</textarea>'
  m = re.search(reg, text)
  if m == None:
    return None
  return m.group(1)

def not_empty(s):
  return s and s.strip()