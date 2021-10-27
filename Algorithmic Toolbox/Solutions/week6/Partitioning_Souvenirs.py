import numpy as np

def partition3(values):
    if (sum(values)%3) == 0:
        W = sum(values)//3
        partition = np.zeros((len(values)+1,W+1,W+1),dtype=int)
        partition[0,:,:]=0
        partition[0,0,0]=1

        for i in range(1,len(values)+1):
            for x in range(0,W+1):
                for y in range(0,W+1):

                    if partition[i-1,x,y]==1:
                        partition[i,x,y] = 1
                    elif x>=values[i-1] and partition[i-1,x-values[i-1],y]==1:
                        partition[i,x,y]=1
                    elif y>=values[i-1] and partition[i-1,x,y-values[i-1]]==1:
                        partition[i,x,y]=1
                    
        
        return partition[-1,-1,-1]
    else:
        return 0
                    


n = int(input())
values = [int(x) for x in input().split()]
print(partition3(values))

