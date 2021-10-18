from random import randint 
def swap(l,i,j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def partition(a,start,end):

    #rand  = randint(start,end)
    #swap(a,rand,end)
    pivot = a[end]
    m1 = start
    same_index = []
    for i in range(start,end):
        
        if a[i]<= pivot:
  
            swap(a,i,m1)
            m1+=1
            if a[i]==pivot:
                same_index.append(i)  
    
    swap(a,m1,end)

    j=0
    for i in range(1,len(same_index)+1): 
        if a[m1-i]!=pivot:
            swap(a,m1-i,same_index[j])
            j+=1
            
    return(m1,m1-len(same_index))



def QuickSort3(a,start,end):
    if start<end:
        m1,m2 = partition(a,start,end)
        QuickSort3(a,start,m2-1)
        QuickSort3(a,m1+1,end) 



n = int(input())
a = [int(x) for x in input().split()]
QuickSort3(a,0,len(a)-1)

print(*a)
