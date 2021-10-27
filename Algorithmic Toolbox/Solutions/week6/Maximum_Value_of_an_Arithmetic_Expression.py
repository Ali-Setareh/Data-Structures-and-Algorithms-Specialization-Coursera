import numpy as np
def separate(s):
    op = ['-','+','*']
    op_list = []
    numbers = []
    for item in s:
        if item in op:
            op_list.append(item)
        else:
            numbers.append(int(item))
    return numbers,op_list 

def do_op(a,b,op):
    if op=='+':
        return a+b 
    elif op=='-':
        return a-b 
    elif op=='*':
        return a*b 

def MinAndMax(M,m,i,j,operations):
    minn = 10**20
    maxx= -10**20
    for k in range(i,j):
        a = do_op(M[i,k],M[k+1,j],operations[k])
        b = do_op(M[i,k],m[k+1,j],operations[k])
        c = do_op(m[i,k],M[k+1,j],operations[k])
        d = do_op(m[i,k],m[k+1,j],operations[k])
        minn = min([minn,a,b,c,d])
        maxx = max([maxx,a,b,c,d])
    return minn,maxx



def parentheses(nubmers,operations):
    n = len(numbers)
    m = np.zeros((n,n),dtype=int)
    M = np.zeros((n,n),dtype=int)
    diag = [(i,i) for i in range(n)]
    for index,x in enumerate(diag):
        
        m[x[0],x[1]] = numbers[index]
        M[x[0],x[1]] = numbers[index]
    
    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s 
            m[i,j],M[i,j] = MinAndMax(M,m,i,j,operations)
        
    return M[0,n-1]

    
s=input()
numbers,operations = separate(s)
print(parentheses(numbers,operations))

