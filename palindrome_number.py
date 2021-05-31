#Link to problem- https://leetcode.com/problems/palindrome-number
def isPalindrome(x: int) -> bool:
        if x<0:
            return 0
        t=x
        n=0
        while t>0:
            n+=1
            t=int(t/10)
        t=x
        rev=0
        while t>0:
            rem=t%10
            t=int(t/10)
            rev+=rem*pow(10,n-1)
            n=n-1
        if rev==x:
            return True
        else:
            return False
