# Maximum Value of the Loot
def get_data(n):
    objects = []
    val_per_w = []
    for i in range(n):
        row = input().split()
        row = [int(x) for x in row]
        row.append(row[0]/row[1])
        objects.append(row)

    return sorted(objects,key=lambda tup: tup[2],reverse=True)



first_inputs = input().split()
c = int(first_inputs[1])
n = int(first_inputs[0])
objects_list = get_data(n)
v=0
while(c!=0 and n!=0):
    a = min(c,objects_list[0][1])
    c = c-a
    v = v+objects_list[0][2]*a
    del objects_list[0]
    n-=1 

print(f'{v:0.4f}')   







