
class bst:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def insert(self,data):
        if data>=self.data:
            if self.right is None:
                self.right=bst(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left=bst(data)
            else:
                self.left.insert(data)
    def print_tree(self,order,c=0):
        if self:
            if c==0:
                if order.lower() in set(['pre','in','post']):
                    print(order+'order traversal: ')
                c+=1
        if order.lower()=='in':
            if self:
                if self.left:
                    self.left.print_tree(order,c)
                print(self.data)
                if self.right:
                    self.right.print_tree(order,c)
            else:
                return
        elif order.lower()=='pre':

            if self:
                print(self.data)
                if self.left:
                    self.left.print_tree(order,c)
                if self.right:
                    self.right.print_tree(order,c)
            else:
                return
        elif order.lower()=='post':

            if self:
                if self.left:
                    self.left.print_tree(order,c)

                if self.right:
                    self.right.print_tree(order,c)
                print(self.data)
            else:
                return
        else:
            print('Wrong Input ')
            return

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print( str(lkpval) + " Not Found")
                return
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(str(lkpval) + " Not Found")
                return
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
def main():
    tree = bst(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.print_tree('pre')
    tree.print_tree('post')
    tree.print_tree('in')
if __name__=='__main__':
    main()


