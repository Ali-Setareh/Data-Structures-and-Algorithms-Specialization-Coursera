#Maximum Advertisement Revenue
n = int(input())
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
s = 0
for x,y in list(zip(a,b)):
    s+=x*y