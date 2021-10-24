import numpy as np

def EditDistance(s1,s2):
    l1 = [i for i in s1]
    l2 = [i for i in s2]
    

    m = len(l1)+1
    n = len(l2)+1
    l1 = ['offset']+l1
    l2 = ['offset']+l2
    D = np.zeros((n,m),dtype=int)

    D[0,1:]=range(1,m)
    D[1:,0]=range(1,n)
    for i in range(1,n):
        for j in range(1,m):
            insertion = D[i-1,j]+1
            delition = D[i,j-1]+1
            mismatch = D[i-1,j-1]+1
            match = D[i-1,j-1]
            if l1[j]==l2[i]:
                D[i,j] = min([insertion,delition,match])
            else:
                D[i,j] = min([insertion,delition,mismatch])
            

        

    return D[-1,-1]


s1 = input()
s2 = input()

print(EditDistance(s1,s2))


