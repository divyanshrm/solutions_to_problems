#link to problem-https://leetcode.com/problems/valid-sudoku/
def isValidSudoku(board):
        def check(arr):
            s=[]
            for x in arr:
                if x =='.':
                    continue
                y=int(x)
                if y in s:
                    return False

                s.append(y)


            return True
        def transpose(l1, l2):
 
            # iterate over list l1 to the length of an item
            for i in range(len(l1[0])):
                # print(i)
                row =[]
                for item in l1:
                    # appending to new list with values and index positions
                    # i contains index position and item contains values
                    row.append(item[i])
                l2.append(row)
            return l2
        trans=transpose(board,[])
        
        for x in range(0,9):
            if not check(board[x]):
                return False
            if not check(trans[x]):
                return False
        import numpy as np
        def c(data):
            i=0
            arr=[]  
            data=np.array(data)
            while(i<len(data)):
                j=0
                while (j<len(data)):

                    p=data[i:i+3,j:j+3]
                    p=np.reshape(p,(-1))

                    arr.append(p)
                    j+=3
                i+=3
            return np.array(arr)
        pol=c(board)
        for x in pol:
            if not check(x):
                return False
        return True