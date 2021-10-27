def merge(left,right,a):
    #print(f'left:{left},right:{right}')

    nl = len(left) 
    nr = len(right)
    i=0
    j=0
    k=0

    global inversions
    while (i<nl and j<nr):
        if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
            inversions+=nl-i
        
        k+=1 
    
    while(i<nl):
        a[k] = left[i]
        i+=1
        k+=1
    while (j<nr):
        a[k] = right[j]
        j+=1
        k+=1
    
   



def mergesort(a):
    n = len(a)
    if n>1:
        mid = n//2
        left = a[:mid]
        right = a[mid:]
        mergesort(left)
        mergesort(right)
        merge(left,right,a)


inversions =0 

#a =  [9,8,7,3,2,1]
n = int(input())
a = [int(x) for x in input().split()]
mergesort(a)
#print(*a)
print(inversions)