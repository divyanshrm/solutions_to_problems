def merge(L,R):
    arr=[]
    i=j=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1
    while i<len(L):
        arr.append(L[i])
        i+=1
    while j<len(R):
        arr.append(R[j])
        
        j+=1
    return arr
        
def sort(arr):
    if len(arr)==1:
        return arr
        
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        L=sort(L)
        R=sort(R)
        ans=merge(L,R)
        return ans
arr=[1,5,3,2,8,6]
print(sort(arr))
print(arr)