import numpy as np 
def LongestSub(s1,s2,s3):
    n = len(s1)
    m = len(s2)
    q = len(s3)
    array = np.zeros((n+1,m+1,q+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(1,q+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    array[i,j,k] = array[i-1,j-1,k-1]+1
                else:
                    array[i,j,k] = max([array[i-1,j,k],array[i,j-1,k],array[i,j,k-1]]) 
    
    return array[-1,-1,-1]

n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()
q = int(input())
s3 = input().split()




print(LongestSub(s1,s2,s3))
