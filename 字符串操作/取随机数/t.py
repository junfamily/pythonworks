import random
a =b=c=d=e=f=g=h=i=j=0
for x in xrange(10000):
    xint = random.randint(0, 9)
    if (xint == 0 ):
        a +=1
    elif (xint == 1 ):
        b +=1
    elif (xint == 2 ):
        c +=1
    elif (xint == 3 ):
        d +=1
    elif (xint == 4 ):
        e +=1
    elif (xint == 5 ):
        f +=1
    elif (xint == 6 ):
        g +=1
    elif (xint == 7 ):
        h +=1
    elif (xint == 8 ):
        i +=1
    elif (xint == 9 ):
        j +=1
    else :
        pass
print a,b,c,d,e,f,g,h,i,j
