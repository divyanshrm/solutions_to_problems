#Link to the problem: https://leetcode.com/problems/add-two-numbers/
def addTwoNumbers(l1, l2):
        def equal(a,b):
            n=len(a)
            m=len(b)
            if n>m:
                while len(a)!=len(b):
                    b.append(0)
            elif m>n:
                while len(a)!=len(b):
                    a.append(0)
            return a,b
        
        a=[]
        b=[]
        x=l1
        y=l2
        while(x!=None):
            a.append(x.val)
            x=x.next
        while(y!=None):
            b.append(y.val)
            y=y.next
        a,b=equal(a,b)
        i=0
        m=0
        n=0
        while(i<len(a)):
            m=m+a[i]*pow(10,i)
            n=n+b[i]*pow(10,i)
            i+=1
        s=m+n
        revs_number = 0  
        number=s
        node=ListNode()
        p=node 
        while (number > 0):   
            remainder = number % 10  
            p.val=remainder
            revs_number = (revs_number * 10) + remainder  
            number = number // 10   
            if number>0:
                t=ListNode()
                p.next=t
                p=p.next
        return node
            
        
    