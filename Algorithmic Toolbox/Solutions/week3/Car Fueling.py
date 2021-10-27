#Car Fueling
d = int(input())
m = int(input())
gass_num = int(input())
gass_corr=[0]
gass_cor_input = input().split()
gass_cor_input = [int(x) for x in gass_cor_input]
gass_corr.extend(gass_cor_input)
gass_corr.append(d)
current=0
num=0
flag=0
while (current<=gass_num):
    last = current
    while(current<=gass_num+1 and gass_corr[current]-gass_corr[last]<=m):
        current+=1
    current-=1
    
    if last==current:
        print(-1)
        flag=1
        break

    if current<=gass_num:
        num+=1

if flag==0:
    print(num)
