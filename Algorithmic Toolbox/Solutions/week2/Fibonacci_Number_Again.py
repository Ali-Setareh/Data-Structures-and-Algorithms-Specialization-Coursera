# Fibonacci_Number_Again
inputs = input().split()
inputs = [int(x) for x in inputs]
n = inputs[0]
m = inputs[1]

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
        print(fib[int(n%period)])
        flag=1
        break
if flag==0:
    print((fib[n-1]+fib[n-2])%m)
