#Collecting_Signatures
n = int(input())
seg = []
for i in range(n):
    seg.append([int(x) for x in input().split()])
#seg = [[4,7],[1,3],[2,5],[5,6]]
seg = sorted(seg,key=lambda x:x[0])

counter=0
num = 0
points=[]
while (counter<n):
    start = seg[counter][0]
    end = seg[counter][1]
    while (1):
        if (counter<n-1 and seg[counter+1][0]<=end):
            counter+=1
            current = seg[counter][0]
        else:
            break
    points.append(current)
    num+=1
    counter+=1
    
print(num)
print(*points)
