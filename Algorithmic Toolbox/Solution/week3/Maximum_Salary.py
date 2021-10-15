def compare(a,b):
    x = int(a+b) 
    y = int(b+a)
    if x>=y:
        return 0
    else:
        return 1
def swap(l,a,b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l
n = int(input())
digits =input().split()
swapped=1
while swapped!=0:
    swapped =0 
    for i in range(n-1):
        
        if (compare(digits[i],digits[i+1])):
            digits = swap(digits,i,i+1)
            swapped+=1


string = ''
for x in digits:
    string+=x 
print(int(string))