#Collecting_Signatures
n = int(input())
seg = []
#a = [int(x) for x in input().split()]
#for i in range(0,len(a),2):
#    seg.append([a[i],a[i+1]])

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
    current = start
    while (1):
        if (counter<n-1 and seg[counter+1][0]<=end):
            counter+=1
            current = seg[counter][0]
            if seg[counter][1]<end:
                end = seg[counter][1]

        else:
            break
    points.append(current)
    num+=1
    #print(current)
    counter+=1
    
print(num)
print(*points)
