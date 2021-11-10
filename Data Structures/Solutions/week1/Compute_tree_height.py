class tree:
    
    def __init__(self,node_num,detail):
        self.node_num = node_num 
        self.node_list = [node() for i in range(node_num)]
        for index,item in enumerate(detail):
            if item !=-1:
                self.node_list[index].parent = item
                self.node_list[item].child.append(index)
                self.node_list[index].index = index

            else:
                self.node_list[index].parent = item
                self.root = index 
                self.node_list[index].index = index

       

    
class node:
    def __init__(self):
        self.parent = None
        self.index = None 
        self.child = []

def height(t):
    h = 0 
    node_count = 0 
    nodes = [t.node_list[t.root]]
    
    while (True):
        node_count = len(nodes)
        if node_count==0:
            return h 
        else:
            h+=1
        
        while (node_count!=0):
            
            for c in nodes[0].child:
                nodes.append(t.node_list[c])
           
            del nodes[0]
            node_count -=1


                








a = tree(int(input()),list(map(int,input().split())))
print(height(a))