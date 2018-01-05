def generateMatrix(n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        imin = 1
        imax = n-1
        jmin = 0
        jmax = n-1
        i = 0
        j = -1
        direct = 0
        for x in range(1,n*n+1):
                if direct==0:
                        j+=1
                        if j==jmax:
                                jmax-=1
                                direct=1
                elif direct==1:
                        i+=1
                        if i==imax:
                                imax-=1
                                direct=2
                elif direct==2:
                        j-=1
                        if j==jmin:
                                jmin+=1
                                direct=3
                elif direct==3:
                        i-=1
                        if i==imin:
                                imin+=1
                                direct=0
                res[i][j] = x
                

        return  res

a = generateMatrix(3)
print(a)
    
