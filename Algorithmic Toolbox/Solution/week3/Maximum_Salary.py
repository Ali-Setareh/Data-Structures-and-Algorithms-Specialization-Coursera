# Maximum Salary
n = int(input())
numbers = [int(x) for x in input().split()]
max_digits = [0,0]
final = ''
while n!=0:
    maximum = -30
    for i in range(n):
        for j in range(i+1,n):
            digit = int(str(numbers[i])+str(numbers[j]))
            if (digit>maximum):
                maximum = digit
                max_digits[0] = numbers[i]
                max_digits[1] = numbers[j]
            digit = int(str(numbers[j])+str(numbers[i]))
            if (digit>maximum):
                maximum = digit
                max_digits[0] = numbers[j]
                max_digits[1] = numbers[i]
    
    
    for item in max_digits:
        numbers.remove(item)
    
    final+=str(maximum)
    n-=2
    if(n==1):
        final+=str(numbers[0])
        break
print(int(final))