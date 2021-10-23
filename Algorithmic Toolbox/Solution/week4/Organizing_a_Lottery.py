from random import randint 
import numpy as np 
def swap(l,i,j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def partition(a,start,end,element):

    rand  = randint(start,end)
    swap(a,rand,end)
    pivot = a[end][element]
    m1 = start
    same_index = []
    for i in range(start,end):
        
        if a[i][element]<= pivot:
            swap(a,i,m1)
            m1+=1
            if a[i][element]==pivot:
                same_index.append(i)
       
    
    swap(a,m1,end)
    j=0
    for i in range(1,len(same_index)+1):
        
        if a[m1-i][element]!=pivot:
            swap(a,m1-i,same_index[j])
            j+=1
            
    return(m1,m1-len(same_index))



def QuickSort3(a,start,end,element):
    
    if start<end:
        m1,m2 = partition(a,start,end,element)
        
       
        
        QuickSort3(a,start,m2-1,element)
        QuickSort3(a,m1+1,end,element) 


#segments = [[randint(0,10),randint(0,10)] for i in range(n)]
#points = [randint(0,10) for i in range(n)]
segments=[]
n = [int(x) for x in input().split()]
for i in range(0,n[0]):
    item =[int(x) for x in input().split()]
    segments.append(item)
points = [int(x) for x in input().split()]


left = [i[0] for i in segments]
right = [i[1] for i in segments]

left = [[x,1] for x in left]
right = [[x,3] for x in right]
points = [[x,2] for x in points]

total=left+points+right

QuickSort3(total,0,len(total)-1,0)

i=0

while (i<=len(total)-2):
    count=0
    if total[i][0]==total[i+1][0]:
        j=i
        while total[j][0] == total[i][0]:
            j+=1
            count+=1
            if j==len(total):
                break
        QuickSort3(total,i,j-1,1)
        i+=count
    if count==0:
        i+=1

dic = {1:'l',2:'p',3:'r'}
string_list = [dic[item[1]] for item in total]


left_p = np.zeros(len(points))
right_p = np.zeros(len(points))


o = 0
for item in string_list:
    if item!='p':
        if item=='l':
            left_p[o:]+=1
        elif item=='r':
            right_p[o:]+=1
    else:
        o+=1
    if o>=len(points):
        break

seg_number=[0]*len(points)
i=0
for x,y in list(zip(left_p,right_p)):
    seg_number[i]=x-y
    i+=1

final_dic={}
index=0
for item in total:
    if item[1]==2:
        final_dic[tuple(item)]=seg_number[index]
        index+=1

for item in points:
    print(int(final_dic[tuple(item)]),end=' ')

