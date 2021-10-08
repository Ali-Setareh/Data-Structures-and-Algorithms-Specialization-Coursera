# Last_Digit_of_the_Sum_of_Squares_of_Fibonacci_Numbers
n = int(input())
m=10
if n<1:
    print(n)
else:
    n+=1
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
            flag=1
            period= i-1
            print((fib[int(n%period)]*fib[int((n-1)%period)])%m)
            break
    if flag==0:
        fib.append((fib[n-1]+fib[n-2])%m)
        print((fib[n]*fib[n-1])%m)