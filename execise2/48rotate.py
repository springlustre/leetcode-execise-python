def rotate(matrix):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
##        1,0 0,2  2,3  3,1
##        x,y   y,a-x+a   a-x+a,a-y+a,  2a-y,x
##        1,0  0,1 1,2 2,1
        length = len(matrix)
        a = (length-1)
        m = (length-1)//2+1
        n = m if length%2==0 else m-1
        for x in range(0,m):
                for y in range(0,n):
                        x1 = y
                        y1 = a-x
                        x2 = y1
                        y2 = a-y
                        x3 = y2
                        y3 = x
                        temp = matrix[x3][y3]
                        matrix[x3][y3] = matrix[x2][y2]
                        matrix[x2][y2] = matrix[x1][y1]
                        matrix[x1][y1] = matrix[x][y]
                        matrix[x][y] = temp
                        
                        
                        

matrix =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
  ]
a = rotate(matrix)
print(matrix)
    
