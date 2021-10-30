def IsBalanced(s):
    stack = []
    openn = ['{','(','[']
    close = ['}',')',']']
    flag=0
    op_index=[]
    for position,char in enumerate(s):  

        if char in openn:
            stack.append(char)
            op_index.append(position)
            flag=1

        elif len(stack)==0:
            flag=0
            
        if char in close:
            
            if flag==1:
                top = stack[-1]
                del stack[-1]
            
            

            if flag==0:
                return (position+1)
            
            elif (top==openn[0] and char!=close[0]) or (top == openn[1] and char!=close[1]) or (top==openn[2] and char!=close[2]) :
                return (position+1)
            else:
                del op_index[-1]
        
           
    if len(stack)==0:
        return ('Success')
    else:
        return (op_index[-1]+1)


s = input()
print(IsBalanced(s))
