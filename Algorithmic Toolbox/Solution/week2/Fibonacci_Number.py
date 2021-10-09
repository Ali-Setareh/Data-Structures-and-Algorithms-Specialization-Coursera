# Fibonacci Number
n = int(input())
if n<=1:
    print(n)
else:
    f = [0]*n
    f[0] = 0 
    f[1] = 1 
    for i in range(2,n):
        f[i] = f[i-1]+f[i-2]

    print(f[n-1]+f[n-2])

