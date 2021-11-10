from math import floor 

def swap(i,j):
    global A,swaplist

    temp = A[i]
    A[i] = A[j]
    A[j] = temp 
    swaplist.append([i,j])
    

def LeftChild(i):
    return 2*i+1

def RightChild(i):
    return 2*i+2

def Parent(i):
    return (i-1)//2

def SiftDown(i,size):
    global A,counter
    minIndex = i 
    l = LeftChild(i)
    

    if l < size and A[l]<A[minIndex]:
   
        minIndex = l 
    

    r = RightChild(i)
    
    if r<size and A[r]<A[minIndex]:
     
        minIndex = r

    if i!=minIndex:
        swap(i,minIndex)
        counter+=1
        SiftDown(minIndex,size) 


def SiftUp(i):
    global A 
    while i>0 and A[Parent[i]]>A[i]:
        swap(Parent[i],i)
        i = Parent(i)

def BuildHeap(A):
    size  = len(A)
    for i in range(size//2,-1,-1):
        SiftDown(i,size)

counter = 0
swaplist=[]
n = int(input())
A = [int(x) for x in input().split()]
BuildHeap(A)
print(counter)
for x,y in swaplist:
    print(x,y)