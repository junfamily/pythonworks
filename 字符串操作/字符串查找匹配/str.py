html = 'asdfasf<title>ddddd</title>dafsdf'

begin=html.find('<title>')+7
end=html[begin:].find('</title>')
str1=html[begin:begin+end]
print str1

print html.find('a')
