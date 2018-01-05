def totalNQueens(n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        board = [["." for _ in range(n)] for i in range(n)]
        f = [0 for _ in range(n)]
        def judge(b,i,j,f):
                for row in range(i):
                        i0 = row
                        j0 = f[i0]
                        if j==j0 or (i-i0)==(j-j0) or (i-i0)==(j0-j):
                                return False
                return True
        def queue(b,i,f,res):
                if i == n:
##                        print("---------",b)
                        return res+1
                r = 0
                for j in range(n):
                        if judge(b,i,j,f):
                                b[i][j] = "Q"
                                f[i] = j
                                r+=queue(b,i+1,f,res)
                                b[i][j] = "."
                return r
                                                       
        result = queue(board,0,f,0)        
        return result

a = totalNQueens(4)
print(a)
    
