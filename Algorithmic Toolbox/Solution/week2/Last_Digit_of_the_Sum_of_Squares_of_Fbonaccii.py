# Last_Digit_of_the_Sum_of_Squares_of_Fibonacci_Numbers
n = int(input())
if n<=1:
    print(n)
else:
    previous = 0 
    current = 1
    for i in range(n):
        temp = current
        current = previous+current
        previous = temp
    
    print(previous*current)