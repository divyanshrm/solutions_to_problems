#Link to the problem: https://leetcode.com/problems/remove-element/
def removeElement(nums, val):
        l=len(nums)
        i=0
        while i <l:
            if nums[i]==val:
                del(nums[i])
                l-=1
                i-=1
            i+=1
        return len(nums)

            
        
    