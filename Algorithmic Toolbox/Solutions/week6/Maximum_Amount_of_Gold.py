import numpy as np 

def KnapSack(W,v):
    value = np.zeros((len(v)+1,W+1),dtype=int)
    value[:,0] = 0 
    value[0,:] = 0 
    for i in range(1,len(v)+1):
        for w in range(1,W+1):
            value[i,w] = value[i-1,w]
            if v[i-1]<=w:
                val = value[i-1,w-v[i-1]] +v[i-1]
                if val>value[i,w]:
                    value[i,w] = val

    return value[-1,-1]


inputs = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]

print(KnapSack(inputs[0],values))


