def DPChange(money,coins):
    minnumcoins = [money+1]*(money+1)
    minnumcoins[0]=0
    for m in range(money+1):
        for coin in coins:
            if coin<=m:
                mincoin = minnumcoins[m-coin]+1
                if mincoin<minnumcoins[m]:
                    minnumcoins[m] = mincoin
    
    return minnumcoins[-1]


money = int(input())
coins = [1,3,4]
print(DPChange(money,coins))
