class node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class bst:
    def __init__(self,root=None):
        self.root=root
    def add(self,val):
        n = node(val)
        if self.root is None:
            self.root = n

        t = self.root
        while not ((t.left is None) and (t.right is None)):
            if t.data > val:
                t = t.left
            elif (t.data<=val):
                t = t.right
            if t is None:
                t=n

        if t.data > val:
            t.left = n
        else:
            t.right = n


x=node(5)
tree=bst(x)
tree.add(3)
print(tree.root.left.data)
tree.add(7)
print(tree.root.right)