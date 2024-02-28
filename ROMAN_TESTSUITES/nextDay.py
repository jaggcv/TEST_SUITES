def nextDay(d,m,y):
    if(d<=30 and m in [1,3,5,7,8,10,12]) or (d<=29 and m in [4,6,9,11]) or (d<=27 and m==2) or (d==28 and m==2 and y%4==0):
        nday=d+1
        nmonth=m
        nyear=y
    elif(d==31 and m in [1,3,5,7,8,10]) or (d==30 and m in [4,6,9,11]) or (d==28 and m==2) or (d==29 and m==2 and y%4==0):
        nday=1
        nmonth=m+1
        nyear=y
    elif(d==31 and m==12):
        nday=1
        nmonth=1
        nyear=nyear+1
    else:
        nday=0
        nmonth=0
        nyear=0
    return nday,nmonth,nyear