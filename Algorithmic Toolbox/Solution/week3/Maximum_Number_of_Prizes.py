#Maximum Number of Prizes
n = int(input())
counter = 1
numbers = []
while counter<=n:
    n-=counter
    numbers.append(counter)
    counter+=1

if n!=0:
    del numbers[-1]
    numbers.append(max(counter,n+counter-1))
print(counter-1)
print(*numbers) 