#link-https://leetcode.com/problems/swapping-nodes-in-a-linked-list
def swapNodes(head: ListNode, k: int) -> ListNode:
        
        def get_length(head):
           
            curr = head
            length = 0
            while curr:
                curr = curr.next
                length += 1

            return length

        def get_to_n(head,n):
            t=head
            c=0
            while c<n-1:

                c+=1
                if c==n-1:
                    prev=t
                t=t.next
            
            return prev,t,t.next
        length=get_length(head)
        if k>length//2:
            k=length-k+1
        if length==1:
            return head
        if length==2:
            t=head.next
            t.next=head
        
            head.next=None
            return t
        if k==1:
            t=head
            prev,n1,ne=get_to_n(head,length)
            n1.next=head.next
            prev.next=head
            head.next=None
            return n1
            
       
        
        
        pre1,n1,ne1=get_to_n(head,k)
        
        pre2,n2,ne2=get_to_n(head,length-k+1)
        
        if length-2*k==0:
            n2.next=n1
            n1.next=ne2
            pre1.next=n2
            
            return head
          
            
        pre1.next=n2
        pre2.next=n1
        n1.next=ne2
        n2.next=ne1
        return head
        