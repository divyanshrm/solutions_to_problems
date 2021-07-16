#link to problem: https://leetcode.com/problems/valid-parentheses
def func(data):
    
    op=['{','[','(']
    cl=['}',']',')']
    stack=[]
    for x in range(len(data)):
        if data[x] in op:
            stack.append(data[x])
        elif data[x] in cl:
            if len(stack)==0:
                return False
            temp=stack.pop()
            temp=op.index(temp)
            if cl[temp]!=data[x]:
                return False
    if len(stack)>0:
        return False
    return True