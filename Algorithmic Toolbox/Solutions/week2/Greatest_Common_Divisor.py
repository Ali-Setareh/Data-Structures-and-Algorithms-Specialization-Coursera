# Greatest Common Divisor
inputs=input()
numbers = [int(x) for x in inputs.split()]
a = numbers[0]
b = numbers[1]
while(b!=0):
    temp = b
    b = a%b 
    a = temp

print(a)