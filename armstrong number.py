for c in range(100,1000):
    s=0
    x=c
    while x>0:
         a=x%10
         x=int(x/10)
         s=s+a**3
    if (s==c):
          print(c)
    
    
