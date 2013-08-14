# -*- coding: utf-8 -*-
import re

page = open('txt.txt', 'r').read()

title = re.findall(r'<title>(.*?)</title>',page)
print title


