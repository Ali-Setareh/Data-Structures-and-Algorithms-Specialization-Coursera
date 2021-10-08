# Last Digit of the Sum of Fibonacci Numbers
n = int(input())
m = 10

previous = 0
current = 1

for i in range(2,n+2):
    temp = current 
    current = (previous+current)%m
    previous = temp
    
if previous+current-1>=0:
    print((previous+current-1)%m)

else:
    print(9)
