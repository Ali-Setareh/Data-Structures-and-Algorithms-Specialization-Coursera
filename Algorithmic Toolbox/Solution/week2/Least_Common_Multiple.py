# Least Common Multiple
inputs=input()
numbers = [int(x) for x in inputs.split()]
a = numbers[0]
b = numbers[1]
while(b!=0):
    temp = b
    b = a%b 
    a = temp

print(int((numbers[0]*numbers[1])/a))