# Binary Search
from math import floor 
def BinarySearchIt(A,low,high,key):
    while low<=high:
        mid = floor((high+low)/2)
        if key == A[mid]:
            return mid 
        elif key<A[mid]:
            high = mid-1 
        else:
            low = mid+1
    return -1

n1 = int(input())
input_1 = [int(x) for x in input().split()]
n2 = int(input())
input_2 = [int(x) for x in input().split()]

result=[]
for i in range(0,n2):
    result.append(BinarySearchIt(input_1,0,n1-1,input_2[i]))

print(*result)

