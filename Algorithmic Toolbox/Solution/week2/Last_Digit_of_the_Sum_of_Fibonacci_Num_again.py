# Last Digit of the Sum of Fibonacci Numbers again
inputs = input().split()
n1 = int(inputs[0])
n2 = int(inputs[1])
n1+=1
n2 +=2
m = 10

previous = 0
current = 1
fib = []
fib.append(previous)
fib.append(current)
flag=0
for i in range(2,n2):
    temp = current 
    current = (previous+current)%m
    previous = temp
    fib.append(current) 
    if current == 1 and previous == 0:
        flag=1
        period= i-1
        if fib[int(n2%period)]>0:
            s2=(fib[int(n2%period)]-1)
           
        else:
            s2 = 9
        
        if fib[int(n1%period)]>0:
            s1=(fib[int(n1%period)]-1)
           
        else:
            s1 = 9
        
        if s2-s1>=0:
            print(s2-s1)
        else:
            print(10+s2-s1)
        
        break
if flag==0:
    fib.append(fib[n2-1]+fib[n2-2])
    if (fib[n2])%m>0:
        s2 = fib[n2]%m-1
    else:
        s2 = 9

    if (fib[n1])%m>0:
        s1 = fib[n1]%m-1
    else:
        s1 = 9 
    
    if s2-s1>=0:
        print(s2-s1)
    else:
        print(s2-s1+10)