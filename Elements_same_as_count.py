a=int(input())
b=list(map(int,input().split()))[:a]
c=[]
for i in b:
    if b.count(i)==i:
        if i not in c:
            c.append(i)
if(c==[]):
    print(-1)
else:
    print(*c)