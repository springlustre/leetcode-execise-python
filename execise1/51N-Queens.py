def solveNQueens(n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        board = [["." for _ in range(n)] for i in range(n)]
        f = [0 for _ in range(n)]
        def judge(b,i,j,f):
                for row in range(i):
                        i0 = row
                        j0 = f[i0]
                        if j==j0 or (i-i0)==(j-j0) or (i-i0)==(j0-j):
                                return False
                return True
        
        def queue(b,i,f):
                if i == n:
##                        print("---------",b)
                        x = []
                        for m in range(n):
                                x.append(''.join(b[m]))
                        res.append(x)
                        return
                
                for j in range(n):
                        if judge(b,i,j,f):
                                b[i][j] = "Q"
                                f[i] = j
                                queue(b,i+1,f)
                                b[i][j] = "."
                                
                                
        queue(board,0,f)
        return res

a = solveNQueens(5)
print(a)
    
