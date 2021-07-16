#link to the problem : https://leetcode.com/problems/squares-of-a-sorted-array/
def sortedSquares(nums):
    """O(N) Solution"""
    if len(nums)==1:
        return [pow(nums[0],2)]
    def merge(x,y):
        n=[]
        i=0
        j=0
        while (i<len(x) and j<len(y)):
            if x[i]<y[j]:
                n.append(x[i])
                i+=1
            else:
                n.append(y[j])
                j+=1
        while i<len(x):
            n.append(x[i])
            i+=1
        while j<len(y):
            n.append(y[j])
            j+=1
        return n
    n=[]
    i=0
    while i <len(nums) and (nums[i]<0):
        i+=1
    n1=[]
    for x in nums[i:]:
        n1.append(pow(x,2))

    n2=[]
    if i>0:
        for x in nums[i-1::-1]:
            n2.append(pow(x,2))


    n.sort()
    return merge(n1,n2)
        