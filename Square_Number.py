n=int(input())
flag=0
for i in range(1,n):
        if (i**2)==n:
            flag=1
            break
if flag==1:
    print("True")
else:
    print("False")