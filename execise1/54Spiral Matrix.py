def spiralOrder(matrix):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        row = len(matrix)
        if row ==0:
                return []
        col = len(matrix[0])
        imax = row-1
        imin = 0
        jmax = col-1
        jmin = 0
        i=0
        j=-1
        direct = 0
        while imin<=imax and jmin<=jmax:
                print(imin,imax,jmin,jmax,i,j)
                if direct ==0:
                        j+=1
                        if j==jmax:
                                direct+=1
                                imin+=1
                                if direct==4:
                                        direct=0
                elif direct==1:
                        i+=1
                        if i==imax:
                                direct+=1
                                jmax -=1
                                if direct==4:
                                        direct=0
                elif direct ==2:
                        j-=1
                        if j==jmin:
                                direct+=1
                                imax -=1
                                if direct==4:
                                        direct=0
                else:
                        i-=1
                        if i==imin:
                                direct+=1
                                jmin +=1
                                if direct==4:
                                        direct=0
                res.append(matrix[i][j])
        return  res

a = spiralOrder([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(a)
    
