#Link to the problem: https://www.geeksforgeeks.org/largest-area-possible-after-removal-of-a-series-of-horizontal-vertical-bars/
#This is my solution
def calc(n,m,h,v):	
	def highest(x,y:list):
	    if len(y)==0:
	        return 0
	    y.sort()
	    cons=1
	    p=0
	    while p <len(y)-1:
	        c=1
	        while p<len(y)-1 and y[p]==y[p+1]-1 :
	            c+=1
	            p+=1
	        if c>cons and y[p]<=x:
	            cons=c
	        p+=1
	    return cons


    hor=highest(n,h)
    ver=highest(m,v)
    
    return(hor+1)*(ver+1)
if __name__='__main__':

	print(calc(10,10,[3,4,5],[2,7,8]))

            
        
    