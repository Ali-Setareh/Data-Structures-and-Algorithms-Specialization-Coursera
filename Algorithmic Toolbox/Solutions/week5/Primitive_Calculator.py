def PrimitiveCalculator(number,operations):
    minnumop = [number+1]*(number+1)
    minnumop[0]=0
    best_operation = [0]*(number+1)
    for m in range(number+1):
        for operation in operations:
            if operations[operation]=='s' and operation<=m:
                minop = minnumop[m-operation]+1
                if minop<minnumop[m]:
                    minnumop[m] = minop
                    best_operation[m] = (operation,operations[operation])
            if operations[operation]=='m' and m%operation==0:
                minop = minnumop[int(m/operation)]+1
                if minop<minnumop[m]:
                    minnumop[m] = minop
                    best_operation[m] = (operation,operations[operation])
    return minnumop[-1]-1,best_operation


n = int(input())
operations = {1:'s',2:'m',3:'m'}
minnum,op = PrimitiveCalculator(n,operations)
#print(op)

x = n
num_between = [n]
while x!=1:
    if op[x][1]=='s':
        x = x - op[x][0]
    else:
        x = int(x/op[x][0])
    
    num_between.append(x)

print(minnum)
print(*num_between[::-1])
