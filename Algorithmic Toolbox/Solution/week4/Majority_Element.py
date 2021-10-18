# Majority element
def majority(a):
    if len(a)==1:
        return a[0]
    mid = len(a)//2
    
    left = majority(a[0:mid])

    right = majority(a[mid:])

    if left == right:
        return left 
    elif count(a,left)> mid:
        return left 
    elif count(a,right)>mid:
        return right

def count(a,x):
    counter=0
    for i in a:
        if i==x:
            counter+=1
    return counter



n = int(input())
a = [int(x) for x in input().split()]
res = majority(a)
if res!=None:
    print(1)
else:
    print(0)

 
