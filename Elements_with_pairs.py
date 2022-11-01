a=int(input())
b=list(map(int,input().split()))[:a]
if(a%2==0):
    print(*b)
else:
    print(*b,end=' 0')