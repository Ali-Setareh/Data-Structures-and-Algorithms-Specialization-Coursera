# Last Digit of the Sum of Fibonacci Numbers
inputs = int(input())
n = inputs+2
m = 10

previous = 0
current = 1
fib = []
fib.append(previous)
fib.append(current)
flag=0
for i in range(2,n):
    temp = current 
    current = (previous+current)%m
    previous = temp
    fib.append(current) 
    if current == 1 and previous == 0:
     
        period= i-1
        if fib[int(n%period)]>0:
            print(fib[int(n%period)]-1)
           
        else:
            print(9)
        flag=1
        break
if flag==0:
    print((fib[n-1]+fib[n-2]-1)%m)
