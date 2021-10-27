# Money Change
coins = [10,5,1]
n = int(input())
num = 0
while n!=0:
    if n<coins[0]:
        del coins[0]
    else:
        d = n//coins[0]
        n-= d*coins[0]
        num+=d
print(num)

