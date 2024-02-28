def gcd(x,y):
    if(x<y):
        x,y=y,x
    if(0==y):
        return x
    if(x%2==0 and y%2==0):
        return 2*gcd(x/2, y/2)
    if(x%2==0):
        return gcd(x/2,y)
    if(y%2==0):
        return gcd(x,y/2)
    return gcd((x+y)/2, (x-y)/2)