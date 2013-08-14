import re

#
name = re.findall(r'<a href="/ls634/" title="(.*?)" ', html)

#
abstract = re.compile(r'<h1>.*?visit',re.DOTALL).findall(res)[0]

#
category[0] = re.compile(r'<.*?>',re.DOTALL).sub('',category1[0]).strip()
