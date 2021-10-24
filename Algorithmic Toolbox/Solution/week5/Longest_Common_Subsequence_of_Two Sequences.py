import numpy as np 
def LongestSub(s1,s2):
    n = len(s1)
    m = len(s2)
    array = np.zeros((n+1,m+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                array[i,j] = array[i-1,j-1]+1
            else:
                array[i,j] = max([array[i-1,j],array[i,j-1]]) 
    
    return array[-1,-1]

n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()

print(LongestSub(s1,s2))
