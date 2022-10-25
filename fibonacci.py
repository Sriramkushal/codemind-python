n=int(input())
n1=0
n2=1
c=0
if (n>0):
    while(c<n):
        print(n1,end=' ')
        n3=n1+n2
        n1=n2
        n2=n3
        c=c+1